# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        res = str(t.val)
        
        if t.left is None and t.right is None:
            return res
        elif t.left is None and t.right is not None:
            res += '()'
            res += '(' + self.tree2str(t.right) + ')'
        elif t.left is not None and t.right is None:
            res += '(' + self.tree2str(t.left) + ')'
        else:
            res += '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        
        return res
