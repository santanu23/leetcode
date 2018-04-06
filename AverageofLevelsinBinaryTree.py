# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        l1 = []
        l2 = []
        l1.append(root)
        res = []
        while l1 or l2:
            current_nodes = []
            while l1:
                curr = l1.pop()
                if curr.left: l2.append(curr.left)
                if curr.right: l2.append(curr.right)
                current_nodes.append(curr.val)
                
            if current_nodes: res.append(current_nodes)
            current_nodes = []
            while l2:
                curr = l2.pop()
                if curr.left: l1.append(curr.left)
                if curr.right: l1.append(curr.right)
                current_nodes.append(curr.val)
            if current_nodes: res.append(current_nodes)
        
        for i in range(len(res)):
            curr_sum = 0
            for j in range(len(res[i])):
                curr_sum += res[i][j]
            
            res[i] = float(curr_sum)/len(res[i])
        
        return res
