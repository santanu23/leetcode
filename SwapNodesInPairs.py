# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode = p0 = ListNode(0)
        dummyNode.next = head
        
        while p0.next and p0.next.next:
          p1, p2 = p0.next, p0.next.next
          p0.next, p1.next, p2.next = p2, p2.next, p1
          p0 = p0.next.next
         
        return dummyNode.next
