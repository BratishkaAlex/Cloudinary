import re


def get_desired_line_from_string(pattern, string):
    return re.search(pattern, string).group(0)
