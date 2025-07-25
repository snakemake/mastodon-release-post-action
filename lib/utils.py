import re


def extract_issue_links(line):
    """
    Formats a changelog line to extract and display issue links, only.
    Will disregard the commit links.
    """
    match_issues = re.findall(
        r"(\[#(\d+)\]\((https?://github\.com/[^)]+issues/\d+)\))", line
    )
    match_commits = re.findall(
        r"(\([a-z0-9]{7,40}\]\((https?://github\.com/[^)]+/commit/[a-z0-9]{7,40})\))",
        line,
    )

    if match_issues:
        if len(match_issues) == 1:
            text_prefix = line.split("(")[0].split("* ")[1].strip()
            # Remove commit links
            if match_commits:
                for commit in match_commits:
                    line = line.replace(commit[0], "")
            return f"* {text_prefix}: {match_issues[0][2]}"
        else:
            issue_links = ", ".join([link[2] for link in match_issues])
            text_prefix = line.split("(")[0].split("* ")[1].strip()
            return f"* {text_prefix}: {issue_links}"

    return line  # Return the original line if no issue links found
