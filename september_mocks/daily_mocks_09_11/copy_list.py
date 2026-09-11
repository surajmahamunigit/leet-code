# 10.44

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        """Make a deep copy of given list and return it.

        Args:
            head (Node): given linked list

        Returns:
            Node: deep copy of given linked list

        Time: O(n) - n = total number of nodes in list
        Space: O(n)
        """

        deep_copy = {None:None}
        curr = head

        # walk all nodes to create new nodes
        while curr:
            new_node = Node(val=curr.val)
            deep_copy[curr] = new_node
            curr = curr.next

        # walk the list again to copy pointers
        curr = head
        while curr:
            deep_copy[curr].next = deep_copy[curr.next]
            deep_copy[curr].random = deep_copy[curr.random]
            curr = curr.next

        return deep_copy[head]

# 10.51