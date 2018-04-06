# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level = [root]
        
        while root and level:
            currentNodes = []
            next_level = []
            for node in level:
                currentNodes.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            ret.append(currentNodes)
            level = next_level
        
        return ret[::-1]
