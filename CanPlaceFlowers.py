class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if self.isValidPlacement(flowerbed, i):
                    n -= 1
                    flowerbed[i] = 1
            i += 1

        if n <= 0:
            return True
        return False
    
    def isValidPlacement(self, flowerbed, i):
        if len(flowerbed) == 1:
            return True
        if i == 0:
            if flowerbed[1] == 0:
                return True
        elif i == len(flowerbed) - 1:
            if flowerbed[len(flowerbed) - 2] == 0:
                return True
        else:
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                return True
        return False
