# 2.39

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        """Make a deep copy of given linked list with random pointer.

        Args:
            head: head node of given linked list

        Returns:
            deep copy of given list

        Time: O(n) - n = number of nodes in original list
        Space: O(n)
        """

        # walk a given list to create new nodes
        curr = head
        deep_copy = {None:None}
        while curr:
            new_node = ListNode(val=curr.val)
            deep_copy[curr] = new_node
            curr = curr.next

        # walk original list again to copy next and random pointers
        curr = head
        while curr:
            deep_copy[curr].next = deep_copy[curr.next]
            deep_copy[curr].random = deep_copy[curr.random]
            curr = curr.next

        return deep_copy[head]

# 2.45 -> 6 min to solve