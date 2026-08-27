# 7.24

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        """Make deep copy of given linked list and return new list.

        Args:
            head: head node of original list

        Returns:
            depp copied linked list

        Time: O(n) - total nodes in original list
        Space: O(n)
        """

        # walk original to create new nodes
        curr = head
        copy_map = {}
        while curr:
            new_node = ListNode(val=curr.val)
            copy_map[curr] = new_node
            curr = curr.next

        # walk original to copy next and random pointer
        curr = head
        while curr:
            copy_map[curr].next = copy_map[curr.next]
            copy_map[curr].random = copy_map[curr.random]
            curr = curr.next

        return copy_map[head]

# 7.30 -> 6 min to solve