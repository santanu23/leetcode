# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        return self.dfs(root,target,float('-inf'),float('inf'))
    
    def dfs(self, node,target,minval,maxval):
        if node is None:
            if (maxval-target > target-minval):
                return minval
            else:
                return maxval

        if target < node.val:
            return self.dfs(node.left,target,minval,node.val)

        return self.dfs(node.right,target,node.val,maxval)
