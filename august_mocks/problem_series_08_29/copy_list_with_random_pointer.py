# 2.33

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        """Make deep copy of given linked list.

        Args:
            head: head node of the given list

        Returns:
            deep copy of given list

        Time: O(n) - n = total nodes in linked list
        Space: O(n)
        """

        deep_copy = {None:None}
        curr = head

        # walk list to create new nodes
        while curr:
            new_node = ListNode(val=curr.val)
            deep_copy[curr] = new_node
            curr = curr.next

        # walk original list again to copy pointers
        curr = head
        while curr:
            deep_copy[curr].next = deep_copy[curr.next]
            deep_copy[curr].random = deep_copy[curr.random]
            curr = curr.next

        return deep_copy[head]

# 2.40 -> 7 min