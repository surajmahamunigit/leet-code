# 11.14

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        """Deep copy linked list with random pointer.

        Args:
            head: head node of given list

        Returns:
            head node of deep copy list

        Time: O(n) - n = length of original linked list
        Space: O(n)
        """

        # walk original list and create new nodes with val and save in map
        curr = head
        node_map = {None:None}
        while curr:
            new_node = ListNode(curr.val)
            node_map[curr] = new_node
            curr = curr.next

        # walk original list again and copy next and random pointer
        curr = head
        while curr:
            node_map[curr].next = node_map[curr.next]
            node_map[curr].random = node_map[curr.random]
            curr = curr.next

        # return head
        return node_map[head]


# 11.27 -> 13 min to finish