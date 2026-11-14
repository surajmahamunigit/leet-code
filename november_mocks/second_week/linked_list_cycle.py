# 10.32

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def has_cycle(self, head: Node|None) -> bool:
        """Find out if the given list has a cycle.

        Args:
            head|None: head node of the given linked list

        Returns:
            boo: True if the list has cycle, else False

        Time complexity: O(n) - n = number of nodes in the list

        Space complexity: O(1)
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
