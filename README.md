# Mastodon Release Post Action

A GitHub Action to automatically post release announcements to Mastodon when a release PR is merged.

## Description

This action monitors your repository for merged pull requests with "release" in the title, and automatically posts an announcement to Mastodon using a preset bot account on the FediScience instance.

## Usage

### Step 1: Create a workflow file

Create a workflow file (e.g. `.github/workflows/announce-release.yml`) in your repository:

```yaml
name: Announce Release on Mastodon

on:
  pull_request:
    types:
      - closed
    branches:
      - main

permissions:
  pull-requests: read

jobs:
  post_to_mastodon:
    if: |
      github.event.pull_request.merged == true &&
      (contains(github.event.pull_request.title, 'release') || contains(github.event.pull_request.title, ' v') || contains(github.event.pull_request.title, 'version'))
    runs-on: ubuntu-latest
    steps:
      - name: Post to Mastodon
        uses: snakemake/mastodon-release-post-action@v1
        with:
          message: |
            Beep, Beep - I am your friendly #Snakemake release announcement bot.
            
            There is a new release of the Snakemake executor for #SLURM on #HPC systems. Its version is {{ version }}!
            
            See {{ changelog }} for details.
            
            Give us some time and you will automatically find the plugin on #Bioconda and #Pypi.
            
            If you want to discuss the release you will find the maintainers here on Mastodon!
            @rupdecat and @johanneskoester
            
            If you find any issues, please report them on {{ issue_url }}
```

### Step 2: Adapt the message

We recomment using a message format like this - the example above is from the executor plugin for SLURM. For your messages, you will need to adapt the description:

```
Beep, Beep - I am your friendly #Snakemake release announcement bot.

There is a new release of the Snakemake executor for <your description>. Its version is {{ version }}!

See {{ changelog }} for details.

Give us some time and you will automatically find the plugin on #Bioconda and #Pypi.

If you want to discuss the release you will find the maintainers here on Mastodon!
<maintainer handles on Moston or indicate BS bridges>

If you find any issues, please report them on {{ issue_url }}
```

You may deviate from this template. Please be sure to mention that this is
- a message of the Snakemake announcement bot and not a message created by humans
- use the available variables
- indicate contact handles