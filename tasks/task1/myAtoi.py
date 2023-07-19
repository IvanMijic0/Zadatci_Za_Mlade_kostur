import re

def myAtoi(s: str) -> int:
    s = s.strip()

    match = re.match(r'^[+-]?\d+', s)

    if match:
        num_str = match.group()
        result = int(num_str)

        result = max(min(result, 2 ** 31 - 1), -2 ** 31)

        return result
    else:
        return 0
