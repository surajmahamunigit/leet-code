# 2.16

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeSortedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge given sorted lists in sorted order.

        Args:
            l1, l2 (ListNode): given sorted lists

        Returns:
            ListNode: merged sorted list

        Time: O(m+n) - m, n = number of nodes in l1 and l2
        Space: O(1)
        """
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 <= val2:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next

# 2.29 -> 13 min