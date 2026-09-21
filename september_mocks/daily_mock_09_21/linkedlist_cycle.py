# 11.36

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        """Determine if the given linkedlist has cycle.

        Args:
            head (ListNode): given linkedlist

        Returns:
            bool: True if the linkedlist has cycle else False

        Time: O(n) - n = total number of nodes

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