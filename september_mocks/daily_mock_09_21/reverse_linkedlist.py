# 11.19

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

        Time: O(n) - n = total number of nodes in given linkedlist

        Space: O(1)
        """

        curr = head
        prev = None

        while curr:
            nex_node = curr.next
            curr.next = prev
            prev = curr
            curr = nex_node

        return prev