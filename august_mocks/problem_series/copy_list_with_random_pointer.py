# 1.47
# given linked list with random poiter, asked to deep copy it and return deep copy
# walk original list and create new nodes with original node values and save it in map as original_node : new_node
# walk original list againa nd attach next and random pointers

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        """Make a deep copy of given linked list with random pointer and return head of new list.

        Args:
            head: head node of original list

        Returns:
            head node of deep copied list

        Time: O(n) - length of given linked list
        Space: O(n)
        """
        curr = head

        # walk list 1st time
        copy_map = {None:None}
        while curr:
            new_node = ListNode(val=curr.val, next=curr.next, random=curr.random)
            copy_map[curr] = new_node
            curr = curr.next

        # walk it second time
        curr = head
        while curr:
            copy_map[curr].next = copy_map[curr.next]
            copy_map[curr].random = copy_map[curr.random]
            curr = curr.next

        return copy_map[head]

# 1.55 -> 8 min to solve