from Queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        curr = pre_head = ListNode(0)
        pq = PriorityQueue()
        for node in lists:
            if node is not None:
                pq.put((node.val, node))
        
        while not pq.empty():
            curr.next = pq.get()[1]
            curr=curr.next
            if curr.next: 
                pq.put((curr.next.val, curr.next))
                
        return pre_head.next
