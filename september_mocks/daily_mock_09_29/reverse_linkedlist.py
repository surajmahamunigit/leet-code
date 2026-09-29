# 10.14

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """Reverse the given linkedlist.

        Args:
            head (ListNode): given linkedlist

        Returns:
            ListNode: reversed linkedlist

        Time complexity: O(n) - n = total number of nodes in given list

        Space complexity: O(1)
        """

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev