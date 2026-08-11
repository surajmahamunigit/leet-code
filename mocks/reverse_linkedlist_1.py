class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linkedlist(self, head: ListNode) -> ListNode:
        """Reverse the given linkedlist and return new head.

        Args:
            head: head node of the list

        Returns:
            head of reversed linked list

        Time: O(n) - n = length of linkedlist
        Space: O(1)
        """
        prev = None
        curr = head
        while curr:
             next_node = curr.next
             curr.next = prev
             prev = curr
             curr = next_node

        return prev
