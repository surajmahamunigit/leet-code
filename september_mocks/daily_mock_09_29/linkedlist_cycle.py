# 10.37

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        """Find out if the given linked list has cycle.

        Args:
            head (ListNode): given linked list

        Returns:
              bool: True if there is a cycle, False otherwise

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(1)
        """

        left = head
        right = head

        while right and right.next:
            left = left.next
            right = right.next.next

            if left == right:
                return True

        return False