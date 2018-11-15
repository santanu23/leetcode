class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                elif i > coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]
