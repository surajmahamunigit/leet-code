# 2.33

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        """Make a deep copy of given list.

        Args:
            head (ListNode): given linked list

        Returns:
            ListNode: copy of linked list

        Time: O(n) - number of nodes in given list
        Space: O(n)
        """

        deep_copy = {None: None}
        curr = head

        # walk list to make new nodes
        while curr:
            new_node = ListNode(curr.val)
            deep_copy[curr] = new_node
            curr = curr.next

        # walk a list again to copy pointers
        curr = head
        while curr:
            deep_copy[curr].next = deep_copy[curr.next]
            deep_copy[curr].random = deep_copy[curr.random]
            curr = curr.next

        return deep_copy[head]

# 2.41 -> 8 min