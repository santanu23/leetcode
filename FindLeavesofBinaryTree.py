# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res =  collections.defaultdict(list)
        self.dfs(root, res)
        return res.values()

    def dfs(self, root, res):
        if not root:
            return 0
        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)
        level = max(left, right) + 1
        res[level] += [root.val]
        return level
    
