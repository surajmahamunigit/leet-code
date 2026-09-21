# 1.01

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copy_list(self, head: ListNode) -> ListNode:
        """Make a deep of copy of given linked list with random pointer.

        Args:
            head (ListNode): given linked list

        Returns:
            ListNode: copy of given linked list

        Time: O(n) - n = total number of nodes in given list

        Space: O(n)
        """

        copy_list = {None:None}
        curr = head

        # walk the list to make new nodes
        while curr:
            new_node = ListNode(val=curr.val)
            copy_list[curr] = new_node
            curr = curr.next

        # walk the list again to copy pointers
        curr = head
        while curr:
            copy_list[curr].next = copy_list[curr.next]
            copy_list[curr].random = copy_list[curr.random]
            curr = curr.next

        return copy_list[head]
