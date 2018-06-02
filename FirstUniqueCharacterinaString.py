class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = [0]*256
        for c in s:
            char_set[ord(c)] = char_set[ord(c)] + 1
        
        for i in range(len(s)):
            if char_set[ord(s[i])] == 1:
                return i
        return -1
