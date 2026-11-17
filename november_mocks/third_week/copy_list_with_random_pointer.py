# 6.52

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copy_list(self, head: ListNode) -> ListNode:
        """Make a deep copy of the given list and return the copy.

        Args:
            head: head node of the given list

        Returns:
            ListNode: head node of the copied list

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(n)
        """

        if head is None:
            return None

        copy = {None: None}

        # First pass: create a copy of every node
        curr = head
        while curr:
            copy[curr] = ListNode(val=curr.val)
            curr = curr.next

        # Second pass: connect the copied nodes
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]