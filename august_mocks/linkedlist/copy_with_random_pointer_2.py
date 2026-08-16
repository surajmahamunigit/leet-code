# 6.11

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        """Make deep copy of given linked list and return its head.

        Args:
            head: head node of given linked list

        Returns:
            head nod eof copied linked list

        Time: O(n) - n = length of linked list
        Space: O(n)
        """

        # walk original list and create new node and add to map
        copy_list = {None:None}

        curr = head
        while curr:
            new_node = Node(curr.val)
            copy_list[curr] = new_node
            curr = curr.next

        # walk original list again and add next and random pointers
        curr = head
        while curr:
            copy_list[curr].next = copy_list[curr.next]
            copy_list[curr].random = copy_list[curr.random]
            curr = curr.next
        return copy_list[head]

# 6.18 -> 7 min to solve