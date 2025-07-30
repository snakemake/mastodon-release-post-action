#!/usr/bin/env python3

import argparse
import logging
import os
import re
import sys

import jinja2
from mastodon import Mastodon
from lib.utils import extract_issue_links


# Convert to Unicode bold (for A-Z, a-z, 0-9)
# we should create the translation table only once:
_UNICODE_BOLD_TRANSLATION = str.maketrans(
    {
        **{chr(i): chr(0x1D400 + i - ord("A")) for i in range(ord("A"), ord("Z") + 1)},
        **{chr(i): chr(0x1D41A + i - ord("a")) for i in range(ord("a"), ord("z") + 1)},
        **{chr(i): chr(0x1D7CE + i - ord("0")) for i in range(ord("0"), ord("9") + 1)},
    }
)


def to_unicode_bold(text: str) -> str:
    """
    Convert ASCII alphanumeric characters in the input text to their Unicode
    bold counterparts.
    """
    return text.translate(_UNICODE_BOLD_TRANSLATION)


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--message", required=True, help="Message to post to Mastodon")
parser.add_argument("--access-token", required=True, help="Mastodon access token")
parser.add_argument("--pr-title", required=True, help="Pull request title")
parser.add_argument(
    "--get-release-notes", action="store_true", help="Get release notes from the PR"
)
parser.add_argument(
    "--image",
    help=(
        "If desired, indicate a repository path to an image to be posted. "
        "Please indicate the name only, e.g., 'image.png'. The action will "
        "look for the image in the repository root. Allowed types are PNG, "
        "JPG(JPEG)."
    ),
)
parser.add_argument(
    "--image-description",
    help=(
        "Indicate a description for the image to be posted. "
        "This will be used as alt text for the image."
    ),
)
# the default base URL is set to FediScience, because we are using it for the
# Mastodon bot but it can be overridden by the user
parser.add_argument(
    "--base-url", default="https://fediscience.org", help="Mastodon base URL"
)
args, unknown = parser.parse_known_args()

logger.debug(f"Unknown arguments: {unknown}")

mastodon_access_token = args.access_token

m = Mastodon(access_token=args.access_token, api_base_url=args.base_url)

pr_title = args.pr_title
if pr_title == "":
    logger.error("PR title is empty")
    sys.exit(1)

match = re.search(r"[Rr]elease\s+([0-9]+\.[0-9]+\.[0-9]+)", pr_title)
if match:
    version = match.group(1)
else:
    logger.error("No version found in PR title")
    sys.exit(1)

# validate version format
if not re.match(r"^[0-9]+\.[0-9]+\.[0-9]+$", version):
    logger.error("Invalid version format")
    sys.exit(1)

# Get repository information
github_repository = os.environ.get("GITHUB_REPOSITORY", "")
repository_url = os.environ.get("REPOSITORY_URL", "")

# If REPOSITORY_URL is not set, try to construct it from GITHUB_REPOSITORY
if not repository_url and github_repository:
    repository_url = f"https://github.com/{github_repository}"
elif not repository_url:
    logger.error(
        "Neither REPOSITORY_URL nor GITHUB_REPOSITORY environment variables are set"
    )
    sys.exit(1)

# Get issue URL if available
issue_url = os.environ.get("ISSUE_URL", f"{repository_url}/issues")

# Determine changelog path/URL
# Check if a custom changelog path is provided
changelog_path = os.environ.get("CHANGELOG_PATH", "")
if changelog_path:
    # Use the provided changelog path
    changelog = f"{repository_url}/{changelog_path}"
else:
    # Try to determine if this is a release tag or a changelog file
    # Default to releases/tag format
    changelog = f"{repository_url}/releases/tag/v{version}"

    # Check if CHANGELOG_FILE environment variable is set
    # Check if CHANGELOG_FILE environment variable is set and not empty
    changelog_file = os.environ.get("CHANGELOG_FILE", "")
    if changelog_file.strip():
        # Use the specified changelog file instead of releases/tag
        changelog = f"{repository_url}/blob/main/{changelog_file}"

# Maximum characters for Mastodon (on FediScience) is 1500
MAX_TOOT_LENGTH = int(os.environ.get("MAX_TOOT_LENGTH", 1500))

# Render the message with all available variables
template = jinja2.Template(args.message)
message = template.render(
    version=version,
    changelog=changelog,
    issue_url=issue_url,
    repository_url=repository_url,
)

# try to extract the release notes from the change log
# first, we need to find the CHANGELOG.md file
changelog_path = None
for root, dirs, files in os.walk(os.getcwd()):
    if "CHANGELOG.md" in files:
        changelog_path = os.path.join(root, "CHANGELOG.md")

release_notes = ""
if changelog_path:
    release_notes = ""
    # now, try to extract the release notes
    with open(changelog_path, "r") as changelog_file:
        changelog_file.readline()  # skip the first line
        for line in changelog_file:
            if line.startswith(f"## [{version}]"):
                # we found the version - now, we need to find the next version
                # and extract the lines in between
                release_notes = []
                for line in changelog_file:
                    if line.startswith("## ["):
                        break
                    # if the line still starts with and number of # reformat to be bold
                    if line.startswith("#"):
                        # Remove all leading # (1 to 4) and whitespace, then make the
                        # rest bold using Unicode bold
                        line = line.lstrip("#").strip()
                        line = to_unicode_bold(line) + "\n"
                    # we also need to extract issue links and paste the plain text link:
                    line = extract_issue_links(line)
                    release_notes.append(line.strip())
                # join the lines and remove leading/trailing whitespace
                release_notes = "\n".join(release_notes).strip()
                break
else:
    logger.warning("CHANGELOG.md file not found")

# next, append the release notes to the message
if release_notes:
    header = "Release Notes (possibly abbriged):"
    # Convert header to Unicode italic (for A-Z, a-z, 0-9)
    italic_map = {
        **{chr(i): chr(0x1D434 + i - ord("A")) for i in range(ord("A"), ord("Z") + 1)},
        **{chr(i): chr(0x1D44E + i - ord("a")) for i in range(ord("a"), ord("z") + 1)},
        **{chr(i): chr(0x1D7CE + i - ord("0")) for i in range(ord("0"), ord("9") + 1)},
    }
    emph_header = "".join(italic_map.get(c, c) for c in header)
    message += "\n" + emph_header + "\n" + release_notes


# check if the message is too long - trim it if necessary
if len(message) > MAX_TOOT_LENGTH:
    message = message[: MAX_TOOT_LENGTH - 3] + "..."
    logger.warning(
        "The received message is too long for the "
        f"Mastodon Robot. We are limited to {MAX_TOOT_LENGTH} "
        "characters. The message has been trimmed."
    )

# post the message
try:
    m.status_post(message)
    # if we have an image path, we post the image as well
    if args.image:
        # first check if the image suffix is of type PNG or JPG(JPEG)
        if not args.image.lower().endswith((".png", ".jpg", ".jpeg")):
            logger.error(
                "Image must be of type PNG or JPG(JPEG). "
                f"Received: {args.image}"
            )
            sys.exit(1)
        # check whether we find an image of that name, for this we walk the current directory
        image_path = None
        for root, dirs, files in os.walk(os.getcwd()):
            if args.image in files:
                image_path = os.path.join(root, args.image)
                break
        if not image_path:
            logger.error(f"Image {args.image} not found in the repository")
            sys.exit(1)
        if args.image_description:
            # post the image with a description
            m.media_post(image_path, description=args.image_description)
        else:
            m.media_post(image_path)
        logger.info(f"Image {args.image_path} posted to Mastodon")
except Exception as e:
    logger.error(f"Failed to post to Mastodon: {e}")
    sys.exit(1)

# report a successful post
logger.info("Message posted to Mastodon")
