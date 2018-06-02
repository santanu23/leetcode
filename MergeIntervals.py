# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        sorted_intervals = sorted(intervals,key= lambda interval:interval.start)
        for interval in sorted_intervals:
            print(interval)
            if res and res[-1].end >= interval.start:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)
        
        return res
