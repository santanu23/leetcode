class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        dp = [0]*len(nums)
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        
        return dp[-1]
