class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res += self.contributeToPerimiter(grid, r, c)
        
        return res
        
        
    def contributeToPerimiter(self, grid, r, c):
        res = 0
        surrounding_tiles = [(r-1,c), (r+1,c), (r,c+1), (r,c-1)]

        for row, col in surrounding_tiles:
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] == 0:
                res += 1

        return res
