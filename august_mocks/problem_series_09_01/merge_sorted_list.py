# 2.57

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge the two sorted lists and return it as a new list.

        Args:
            l1, l2: given sorted lists

        Returns:
            merged sorted list

        Time: O(m+n) - m, n = total number of nodes in l1 and l2
        Space: O(1)
        """

        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            if val1 <= val2:
                curr.next = l1
                l1 = l1.next if l1 else None
            else:
                curr.next = l2
                l2 = l2.next if l2 else None

            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next

# 3.03