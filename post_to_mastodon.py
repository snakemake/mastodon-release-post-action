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


# construct changelog URL with proper quoting
changelog="https://github.com/snakemake/snakemake-executor-plugin-slurm/releases/tag/v${version}"

# Maximum characters for Mastodon (on FediScience) is 1500
MAX_TOOT_LENGTH = 1500

# render the message and replace the changelong
template = jinja2.Template(args.message)
message = template.render(version=version, changelog=changelog)

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

