class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}

        for i, num in enumerate(nums):
            if target-num in index_dict:
                return [index_dict[target-num], i]
            index_dict[num] = i
