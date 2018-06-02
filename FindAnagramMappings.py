class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(B)):
            d[B[i]] = i
        res = []
        for i in range(len(A)):
            res.append(d[A[i]])
        
        return res
