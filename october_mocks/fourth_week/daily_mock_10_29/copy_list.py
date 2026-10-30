# 11.13

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copy_list(self, head: ListNode|None) -> ListNode|None:
        """Copy given list with random pointer.

        Args:
            head (ListNode|None): head node of the given list.

        Returns:
              ListNode|None: head node of the copied list

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(n)
        """

        copy = {None:None}

        # walk list to create new nodes
        curr = head
        while curr:
            new_node = ListNode(val=curr.val)
            copy[curr] = new_node
            curr = curr.next

        # walk a list again to copy next and random pointer
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]

# 11.21 -> 8 minute sto write solution. didnt know how to write build_list and values_to_list function for list with random and next pointer
# git commit -> feat: add copy linked list with random solution