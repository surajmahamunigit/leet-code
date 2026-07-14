class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Args:
            head: head of list

        Returns:
            True if list is cyclic, otherwise False

        Time: O(n) - n i s length of list
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
