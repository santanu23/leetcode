# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ordered = self.inOrder(root)
        for i in range(len(ordered)-1):
            if ordered[i+1] <= ordered[i]:
                return False
        
        return True
        
        
    def inOrder(self, root):
        if not root:
            return []

        return self.inOrder(root.left) + [root.val] +  self.inOrder(root.right)
