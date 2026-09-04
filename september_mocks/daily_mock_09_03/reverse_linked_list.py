# 6.52

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """Reverse the given linked list.

        Args:
            head (ListNode): head node of the given linked list

        Returns:
            ListNode: reversed linked list

        Time: O(n) - n = total number of nodes
        Space: O(1)
        """

        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev