# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        levels= collections.defaultdict(list)
        self.levelOrderTraversal(root,0,levels)
        for level in levels.values():
            for i in range(len(level)):
                level[i-1].next = level[i]
            
            level[i].next = None
        
    def levelOrderTraversal(self, root, level, levels):
        if not root:
            return

        levels[level] += [root]
        self.levelOrderTraversal(root.left, level + 1, levels)
        self.levelOrderTraversal(root.right, level + 1, levels)
