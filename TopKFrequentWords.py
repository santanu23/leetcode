import heapq as hq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count_dict = {}
        for word in words:
            count_dict[word] = count_dict.get(word,0) + 1
        
        pq = []
        hq.heapify(pq)
        
        for word,count in count_dict.items():
            hq.heappush(pq,(-count,word))
        
        res = []
        for _ in range(k):
            res.append(str(hq.heappop(pq)[1]))
        
        return res
