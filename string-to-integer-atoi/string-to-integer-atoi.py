import string
import re


class Solution:
    pattern = re.compile("^\s*(?P<value>[+-]?\d+).*$")

    def myAtoi(self, s: str) -> int:
        result = re.match(self.pattern, s)
        if result:
            value = int(result.group("value"))
        else:
            value = 0

        lower_bound = -(2 ** 31)
        upper_bound = (2 ** 31) - 1
        if value < lower_bound:
            return lower_bound
        elif upper_bound < value:
            return upper_bound
        return value
