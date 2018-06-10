class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(m) for _ in range(n)]
        
        for row in range(n):
            dp[row][0] = 1
        
        for col in range(m):
            dp[0][col] = 1
        
        for row in range(1,n):
            for col in range(1,m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        print(dp)
        
        return dp[n-1][m-1]
