# 10.20

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_linkedlists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge the two given sorted linked lists and return head.

        Args:
            l1, l2 (ListNode): given sorted linked lists

        Returns:
            ListNode: head of the merged linked list

        Time complexity: O(m+n) - m, n = total number of nodes in l1 and l2

        Space complexity: O(1)
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