# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = collections.defaultdict(list)
        self.levelOrderTraversal(root, 0, res)
        return [val[0] for val in res.values()]
        
        
    def levelOrderTraversal(self, root, level, res):
        if not root:
            return
        
        res[level] += [root.val]
        self.levelOrderTraversal(root.right, level+1, res)
        self.levelOrderTraversal(root.left, level+1, res)
