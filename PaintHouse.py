class Solution(object):
    def minCost(self, costs, used=0):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        min_r, min_g, min_b = [0]*3
        
        for cost in costs:
            r, b, g = cost

            new_min_r, new_min_g, new_min_b = min_r, min_g, min_b

            new_min_r = min(min_g, min_b) + r
            new_min_b = min(min_r, min_g) + b
            new_min_g = min(min_r, min_b) + g

            min_r, min_b, min_g = new_min_r, new_min_b, new_min_g

        return min(min_r, min_b, min_g)
