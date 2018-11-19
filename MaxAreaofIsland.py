class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        global_max = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                local_max = 0
                if grid[row][col] == 1:
                    local_max = self.dfs(grid, visited, row, col)
            
                global_max = max(local_max, global_max)
        
        return global_max

    def dfs(self, grid, visited, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        
        if (row, col) in visited:
            return 0
        
        visited.add((row, col))
        
        if grid[row][col] == 0:
            return 0
        
        return self.dfs(grid, visited, row + 1, col) + \
               self.dfs(grid, visited, row - 1, col) + \
               self.dfs(grid, visited, row, col + 1) + \
               self.dfs(grid, visited, row, col - 1) + 1
        
