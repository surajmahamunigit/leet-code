# 8.11

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode|None, l2: ListNode|None) -> ListNode|None:
        """Add given two non-negative numbers.

         Args:
             l1: first number
             l2: second number

         Returns:
             ListNode|None: result of addition of two numbers stored in reverse order

         Time complexity: O(max(L1,L2)) - L1, L2 = total number of nodes in list l1 and l2

         Space complexity: O(max(L1, L2))
         """

        carry = 0
        dummy = ListNode()
        tail = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_sum = val1 + val2 + carry
            carry = curr_sum // 10
            digit = curr_sum % 10

            tail.next = ListNode(val=digit)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next