# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return 
        
        curr = head
        while curr:
            res = RandomListNode(curr.label)
            temp = curr.next
            curr.next = res
            res.next = temp
            curr = res.next
            res = res.next
        
        res = head.next
        curr = head
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
        
        curr = head
        while curr:
            try:
                temp = curr.next
                curr.next = curr.next.next
                curr = temp
            except:
                break
            
        return res
