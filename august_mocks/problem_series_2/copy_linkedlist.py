# 10.15
# given head of original list, asked to make deep copy of it
# walk original list to create new nodes with same values
# walk again to copy, two pointers

class Node:
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        """Make deep copy of given linked list with random pointer.

        Args:
            head: head node of original list

        Returns:
            head node of copied linked list

        Time: O(n) - n = length of given linked list
        Space: O(n)
        """

        copy_map = {None: None}     # for pointers

        # walk first time to create new nodes with values
        curr = head
        while curr:
            new_node = Node(val=curr.val)
            copy_map[curr] = new_node
            curr = curr.next

        # walk again to copy pointers
        curr = head
        while curr:
            copy_map[curr].next = copy_map[curr.next]
            copy_map[curr].random = copy_map[curr.random]
            curr = curr.next

        return copy_map[head]

# 10.23 -> 8 min to solve