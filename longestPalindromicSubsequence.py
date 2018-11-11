
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = [[0]*len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        for k in range(1,len(s)):
            i = 0
            j = k
            while j < len(s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                i += 1
                j += 1
        
        return dp[0][len(s)-1]
