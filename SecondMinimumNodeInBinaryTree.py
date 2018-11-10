# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lowest = float('inf')
        second_lowest = float('inf')
        res = self.dfs(root,lowest,second_lowest)

        if res == float('inf'):
            return -1
    
        return res
        
        
    def dfs(self, root, lowest, second_lowest):
        if not root:
            return second_lowest

        if lowest < root.val < second_lowest:
            second_lowest = root.val

        if root.val < lowest:
            lowest = root.val

        second_lowest_left = self.dfs(root.left, lowest, second_lowest,)
        second_lowest_right = self.dfs(root.right, lowest, second_lowest)

        return min(second_lowest_left, second_lowest_right)
