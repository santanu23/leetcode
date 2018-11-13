class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        dp = [0]*(target+1)
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                elif i == num:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-num]
        
        return dp[-1]
