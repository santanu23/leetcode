# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=collections.defaultdict(list)
        self.dfs(root, res)
        return [max(level) for level in res.values()]
        
    def dfs(self, root, res, level=0):
        if not root:
            return

        res[level] += [root.val]
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)
