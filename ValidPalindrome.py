import string
import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha_numeric = "".join(re.findall(r'\w', s)).lower()
        return alpha_numeric == alpha_numeric[::-1]
