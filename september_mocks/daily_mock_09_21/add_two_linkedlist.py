# 1.24

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add the given two list and return the result in same format.

        Args:
            l1, l2 (ListNode): given numbers in linked list form

        Returns:
            ListNode: result of addition in linkedlist form

        Time: O(m+n) - m, n = number of nodes in l1 and l2

        Space: O(m+n)
        """

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_sum = l1.val + l2.val + carry
            carry = curr_sum // 10
            digit = curr_sum % 10
            new_node = ListNode(val=digit)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next