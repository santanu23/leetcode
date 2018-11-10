class Solution(object):
    def climbStairsRecursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            return n
        
        return self.climbStairsRecursive(n-1) + self.climbStairsRecursive(n-2)

    def climbStairsDPTopDown(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            memo[n] = n
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairsDPTopDown(n-1) + self.climbStairsDPTopDown(n-2)
        
        return memo[n]
    
    def climbStairsDPBottomUp(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        dp = [0]*n
        
        dp[0] = 1
        dp[1] = 2

        for i in range(2,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
