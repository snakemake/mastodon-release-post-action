from post_to_mastodon import extract_issue_links

def test_single_issue_link():
    line = "* measuring compute efficiency per job ([#221](https://github.com/snakemake/snakemake-executor-plugin-slurm/issues/221)) ([3cef6b7](https://github.com/snakemake/snakemake-executor-plugin-slurm/commit/3cef6b7889c8ba09280f345bade3497b144bedc7))"
    expected = "* measuring compute efficiency per job https://github.com/snakemake/snakemake-executor-plugin-slurm/issues/221"
    assert extract_issue_links(line) == expected

def test_multiple_issue_links():
    line = "* Fixed bug in feature X ([#123](https://github.com/example/repo/issues/123)) and improved performance ([#456](https://github.com/example/repo/issues/456))"
    expected = "* Fixed bug in feature X: https://github.com/example/repo/issues/123, https://github.com/example/repo/issues/456"
    assert extract_issue_links(line) == expected

def test_no_issue_links():
    line = "* Documentation updates (no issues)"
    assert extract_issue_links(line) == line

def test_single_issue_and_commit():
    line = "* Another fix ([#789](https://github.com/test/project/issues/789)) (commit hash)"
    expected = "* Another fix https://github.com/test/project/issues/789"
    assert extract_issue_links(line) == expected

def test_multiple_issues_and_commit():
    line = "* multiple issues ([#221](https://github.com/snakemake/snakemake-executor-plugin-slurm/issues/221)) ([#222](https://github.com/snakemake/snakemake-executor-plugin-slurm/issues/222)) ([3cef6b7](https://github.com/snakemake/snakemake-executor-plugin-slurm/commit/3cef6b7889c8ba09280f345bade3497b144bedc7))"
    expected = "* multiple issues: https://github.com/snakemake/snakemake-executor-plugin-slurm/issues/221, https://github.com/snakemake/snakemake-executor-plugin-slurm/issues/222"
    assert extract_issue_links(line) == expected

def test_issue_link_at_start_of_line():
    line = "([#1](https://github.com/example/repo/issues/1)) This is a test."
    expected = "https://github.com/example/repo/issues/1 This is a test."
    assert extract_issue_links(line) == expected