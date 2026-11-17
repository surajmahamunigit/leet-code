# 6.18

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node_from_end(self, head: ListNode|None, n: int) -> ListNode|None:
        """Remove the nth node from the end of the list.

        Args:
            head: head node of the given list
            n: 1-based position from the end of the list to remove

        Returns:
            ListNode|None: Head of the list after removal

        Time complexity: O(L) - L = total number of nodes in the given list

        Space complexity: O(1)
        """

        dummy = ListNode(next=head)
        slow = dummy
        fast = head

        # move the fast pointer n nodes ahead
        while fast and n > 0:
            fast = fast.next
            n -= 1

        # move slow and fast
        while fast:
            slow = slow.next
            fast = fast.next

        # remove nth node
        slow.next = slow.next.next

        return dummy.next