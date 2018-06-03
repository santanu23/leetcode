class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = []
        for i in range(len(grid)):
            visited.append([0]*len(grid[i]))
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and visited[row][col] == 0:
                    self.findIsland(grid,visited,row,col)
                    res += 1
        
        return res
    
    def findIsland(self,grid,visited,row,col):
        if row < 0 or row >= len(grid):
            return
        elif col < 0 or col >= len(grid[0]):
            return
        else:
            #we are in proper bounds
            if visited[row][col] == 1:
                #we have already visited this node
                return
            else:
                #this is unexplored teritory
                visited[row][col] = 1 #mark current as visited
                if grid[row][col] == "1":
                    self.findIsland(grid,visited,row-1,col) #visit up
                    self.findIsland(grid,visited,row+1,col) #visit down
                    self.findIsland(grid,visited,row,col-1) #visit left
                    self.findIsland(grid,visited,row,col+1) #visit right
        return
        
            
            
            
