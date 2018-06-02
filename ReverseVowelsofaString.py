class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        res = list(s)
        vowels = ["a","e","i","o","u","y"]
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                res[i], res[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] in vowels and s[j] not in vowels:
                res[j] = s[j]
                j -= 1
            elif s[j] in vowels and s[i] not in vowels:
                res[i] = s[i]
                i += 1
            else:
                res[i], res[j] = s[i], s[j]
                i += 1
                j -= 1
        return "".join(res)
