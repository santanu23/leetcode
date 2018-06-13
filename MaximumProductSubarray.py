class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        max_pos_product = [0]*len(nums)
        max_pos_product[0] = nums[0]
        max_neg_product = [0]*len(nums)
        max_neg_product[0] = nums[0]
        
        for i in range(1,len(nums)):
            product1 = max_pos_product[i-1]*nums[i]
            product2 = max_neg_product[i-1]*nums[i]
            
            max_pos_product[i] = max(product1,max(product2,nums[i]))
            max_neg_product[i] = min(product1,min(product2,nums[i]))
            
        return max(max_pos_product)
