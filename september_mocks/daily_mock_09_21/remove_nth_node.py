# 12.48

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node(self, head: ListNode, n: int) -> ListNode:
        """Remove the nth node from the end of given list.

        Args:
            head (ListNode): given linkedlist

        Returns:
            ListNode: remove the nth node from the given list and returns

        Time: O(n) - n = total number of nodes in linkedlist

        Space: O(1)
        """

        dummy = ListNode(next=head)
        left = dummy
        right = head

        while right and n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next