# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inOrderTraversal(root)[k-1]
        
    def inOrderTraversal(self, root):
        if not root:
            return []

        return self.inOrderTraversal(root.left) + [root.val] + self.inOrderTraversal(root.right)
