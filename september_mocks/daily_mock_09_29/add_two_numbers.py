# 5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers given as linked list.

        Args:
            l1, l2 (ListNode): two numbers given as linked list

        Returns:
            ListNode: addition of two numbers as linked list

        Time complexity: O(max(m,n)) - m, n = total number of nodes in l1 and l2

        Space complexity: O(max(m, n))
        """

        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_sum = carry + val1 + val2
            carry = curr_sum // 10
            digit = curr_sum % 10

            new_node = ListNode(val=digit)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next