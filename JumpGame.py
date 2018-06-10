class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        for i in range(len(nums)):
            if max_jump < i:
                return False
            max_jump = max(max_jump,i+nums[i])
        else:            
            return True
