#!/usr/bin/env python3

import argparse
import logging
import os
import re
import sys

import jinja2
from mastodon import Mastodon

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--message", help="Message to post to Mastodon")
args = parser.parse_args()

# Configure Mastodon connection
mastodon_access_token = os.environ.get("MASTODON_ACCESS_TOKEN")
mastodon_base_url = os.environ.get("MASTODON_BASE_URL", "https://fediscience.org")

if not mastodon_access_token:
    logger.error("MASTODON_ACCESS_TOKEN environment variable not set")
    sys.exit(1)

m = Mastodon(access_token=os.environ["MASTODON_ACCESS_TOKEN"],
                      api_base_url="https://fediscience.org")

pr_title = os.environ["PR_TITLE"]
if pr_title == "":
    logger.error("PR_TITLE is empty")
    sys.exit(1)

match = re.search(r'[Rr]elease\s+([0-9]+\.[0-9]+\.[0-9]+)', PR_TITLE)
if match:
    version = match.group(1)
else:
    logger.error("No version found in PR_TITLE")
    sys.exit(1)

# validate version format
if not re.match(r'^[0-9]+\.[0-9]+\.[0-9]+$', version):
    logger.error("Invalid version format")
    sys.exit(1)

# Get repository information
github_repository = os.environ.get("GITHUB_REPOSITORY", "")
repository_url = os.environ.get("REPOSITORY_URL", "")

# If REPOSITORY_URL is not set, try to construct it from GITHUB_REPOSITORY
if not repository_url and github_repository:
    repository_url = f"https://github.com/{github_repository}"
elif not repository_url:
    logger.error("Neither REPOSITORY_URL nor GITHUB_REPOSITORY environment variables are set")
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
    changelog_file = os.environ.get("CHANGELOG_FILE", "CHANGELOG.md")
    if changelog_file:
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
    repository_url=repository_url
)

# check if the message is too long
if len(message) > MAX_TOOT_LENGTH:
    logger.error("The received message is too long for the Mastodon Robot. We are limited to 1500 characters.")
    sys.exit(1)

# post the message
try:
    m.status_post(message)
except Exception as e:
    logger.error(f"Failed to post to Mastodon: {e}")
    sys.exit(1)

# report a successful post
logger.info("Message posted to Mastodon")

