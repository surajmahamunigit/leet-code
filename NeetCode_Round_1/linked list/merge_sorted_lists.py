class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def mergerTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Args:
            l1: head of list 1
            l2: head of list 2

        Returns:
            merged sorted list

        Time: O(m + n) - m = number of nodes in list 1, n = number of nodes in list 2
        Space: O(1)
        """

        dummy = ListNode()
        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # for remaining list
        if l1:
            tail.next = l1

        elif l2:
            tail.next = l2

        return dummy.next