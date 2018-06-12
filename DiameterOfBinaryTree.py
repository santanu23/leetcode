# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def get_depth(node):
            if not node:
                return 0
            left, right = get_depth(node.left), get_depth(node.right)
            self.res = max(self.res,left+right)
            return max(left,right) + 1
        
        
        get_depth(root)
        return self.res
