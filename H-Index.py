class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations,reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if citations[i] > i:
                h_index += 1
    
        return h_index
