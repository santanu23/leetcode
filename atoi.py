import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        try:
            int_min = -2147483648
            int_max = 2147483647
            n = int(re.findall('(^[\\+\\-0]*\\d+)\\D*', str.strip())[0])
            return int_min if n < int_min else int_max if n > int_max else n
        except:
            return 0
