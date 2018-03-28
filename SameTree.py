class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif q is None and p is not None:
            return False
        else:
            return p.val == q.val\
                   and self.isSameTree(p.left,q.left) \
                   and self.isSameTree(p.right,q.right)
