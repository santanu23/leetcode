class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if is_palindrome(s[i:j]):
                    res.append(s[i:j])
                    
        return res
        
    def is_palindrome(self,s):
        return s == s[::-1]
