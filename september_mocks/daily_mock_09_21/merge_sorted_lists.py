# 11.23

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_sorted_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted lists in sorted order.

        Args:
            l1, l2 (ListNode): given sorted lists

        Returns:
            ListNode: merged list in sorted order

        Time: O(m+n) - m, n = total number of nodes in given lists

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
