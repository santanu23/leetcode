def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    res = []
    visited = []
    for i in range(len(matrix)):
        visited.append([0]*len(matrix[i]))
    
    print(visited)
    helper(matrix,visited,0,0,"r",res)
    return res

def helper(matrix,visited,row,col,direction,res):
    if visited[row][col] == 1:
        return
    visited[row][col] = 1
    res.append(matrix[row][col])
    if direction == "r":
        if col == len(matrix[0]) - 1 or visited[row][col+1] == 1:
            direction = "d"
            helper(matrix,visited,row+1,col,direction,res)
        else:
            helper(matrix,visited,row,col+1,direction,res)
    elif direction == "d":
        if row == len(matrix) - 1 or visited[row+1][col] == 1:
            direction = "l"
            helper(matrix,visited,row,col-1,direction,res)
        else:
            helper(matrix,visited,row+1,col,direction,res)
    elif direction == "l":
        if col == 0 or visited[row][col-1] == 1:
            direction = "u"
            helper(matrix,visited,row-1,col,direction,res)
        else:
            helper(matrix,visited,row,col-1,direction,res)
    elif direction == "u":
        if row == 0 or visited[row-1][col] == 1:
            direction = "r"
            helper(matrix,visited,row,col+1,direction,res)
        else:
            helper(matrix,visited,row-1,col,direction,res)

input_arr = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print(spiralOrder(input_arr))
