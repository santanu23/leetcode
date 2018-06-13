import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num,0) + 1
        
        pq = []
        heapq.heapify(pq)
        
        for num,count in count_dict.items():
            heapq.heappush(pq,(-count,num))
        
        res = []
        
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        
        return res
        
