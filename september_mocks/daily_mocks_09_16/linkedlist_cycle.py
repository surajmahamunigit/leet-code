# 7.04

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """Find if there is cycle in the given linked list.

        Args:
            head (ListNode): given linked list.

        Returns:
            bool: True if hasCycle, False otherwise.

        Time: O(n) - n = total number of nodes in the linked list.
        Space: O(1)
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False