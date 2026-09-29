# 4.17

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def deep_copy_list(self, head: ListNode) -> ListNode:
        """Make deep copy of given linked list.

        Args:
            head (ListNode): given linked list

        Returns:
            ListNode: deep copied list

        Time complexity: O(n) - n = total number of nodes in given list

        Space complexity: O(n)
        """

        copy = {None:None}

        # walk the list to create nodes
        curr = head
        while curr:
            new_node = ListNode(val=curr.val)
            copy[curr] = new_node
            curr = curr.next

        # walk the list again to copy pointers
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]