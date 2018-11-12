# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, root)
    
    def dfs(self, root1, root2):
        if not root1 and not root2:
            return True

        if root1 and not root2 or \
           root2 and not root1 or \
           root1.val != root2.val:
            return False
        
        return self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left) 
