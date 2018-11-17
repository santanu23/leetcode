# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.inOrderTraversal(root)
        min_val = float('inf')
        for i in range(1, len(res)):
            min_val = min(min_val, res[i] - res[i-1])
        return min_val
        
        
        
    def inOrderTraversal(self, root):
        if not root:
            return []

        return self.inOrderTraversal(root.left) + [root.val] + self.inOrderTraversal(root.right)
