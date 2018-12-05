# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(path+str(root.val))
        if root.left:
            self.dfs(root.left, path + str(root.val) + '->', res)
        if root.right:
            self.dfs(root.right, path + str(root.val) + '->', res)
