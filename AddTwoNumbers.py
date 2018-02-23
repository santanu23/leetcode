# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number1 = self._linkedListToNumber(l1)
        number2 = self._linkedListToNumber(l2)
        return self._numberToLinkedList(number1+number2)
        
    def _linkedListToNumber(self,linked_list):
        res = []
        while linked_list:
            res.append(str(linked_list.val))
            linked_list = linked_list.next
        return int("".join(res)[::-1])

    def _numberToLinkedList(self,number):
        res = head = ListNode(0)
        for c in str(number)[::-1]:
            res.next = ListNode(int(c))
            res = res.next
        return head.next
