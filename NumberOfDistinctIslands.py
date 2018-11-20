class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    current_island=set()
                    self.search(grid, visited, row, col, current_island, row, col)
                    if current_island:
                        islands.add(tuple(current_island))
        
        return len(islands)
        
    def search(self, grid, visited, r, c, current_island, r0, c0):
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) \
           and (r,c) not in visited and grid[r][c] == 1:
            visited.add((r,c))
            current_island.add((r-r0,c-c0))
            self.search(grid, visited, r+1, c, current_island, r0, c0)
            self.search(grid, visited, r-1, c, current_island, r0, c0)
            self.search(grid, visited, r, c+1, current_island, r0, c0)
            self.search(grid, visited, r, c-1, current_island, r0, c0)
