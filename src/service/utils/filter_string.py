import re
from typing import Optional


def filter_string_list(filtered_strings: list[str], good_patterns: list[str], bad_patterns: Optional[list[str]] = None):

    """
    Фильтрация строк.
    """

    result: list[str] = []

    good_string: list[str] = []

    if good_patterns:
        for link in filtered_strings:
            for regex in good_patterns:
                if re.search(regex, link, re.IGNORECASE):
                    good_string.append(link)
    else:
        good_string = filtered_strings.copy()
    if bad_patterns:
        for found_link in good_string:
            if not any([re.search(regex, found_link, re.IGNORECASE) for regex in bad_patterns]):
                result.append(found_link)
        return result
    else:
        return good_string
