class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = [int(y) for y in str(int("".join([str(x) for x in digits]))+1)]
        return [0]*(len(digits) - len(res)) + res
