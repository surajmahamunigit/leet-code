# 9.20

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """Make a deep cpy of the given list with next and random pointer.

        Args:
            head (Node): head of the given linked list

        Returns:
             Node: head node of the deep copied linked list

        Time complexity: O(n) - n = total number of nodes in the linked list

        Space complexity: O(n)
        """

        copy = {None:None}

        # walk the list to create new nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            copy[curr] = new_node
            curr = curr.next

        # walk the list again to copy both pointers
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]

# 9.25 -> 5 minutes to solve the problem
# git commit suggestion -> feat: add copy linked list with random pointer solution
