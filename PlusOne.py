class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = [int(y) for y in str(int("".join([str(x) for x in digits]))+1)]
        return [0]*(len(digits) - len(res)) + res
        
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(c) for c in str(int(reduce(lambda x,y:x+y,[str(d) for d in digits]))+1)]
