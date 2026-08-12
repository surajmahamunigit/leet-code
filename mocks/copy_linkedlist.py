# algorithm
# given a linked list and we are asked to copy it node by node and return its head node
# first we will traverse the given linked list noded by node and create new nodes with their val == given node val
# and then save it map as given/current node = new_node(val)
# then traverse given linked list again from head node -> use each node as key to get new_node, then set its remaining values


class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copy_linkedlist(self, head: ListNode) -> ListNode:
        """Deep copy linked list.

        Args:
            head: head node of the linked list

        Returns:
            head node of deep copy linked list

        Time: O(n) - n = length of linked list
        Space: O(n))
        """
        new_list = {None: None,}
        # walk the original list -> create new nodes -> save in the map {original : new}
        curr = head
        while curr:
            new_node = ListNode(curr.val)
            new_list[curr] = new_node
            curr = curr.next


        # walk again -> wire next and random for each copy
        curr = head
        while curr:
            new_node = new_list[curr]
            new_node.next = new_list[curr.next]
            new_node.random = new_list[curr.random]
            curr = curr.next

        return new_list[head]























