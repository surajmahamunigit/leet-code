# 9.19

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two linked list representing numbers in reverse order.

        Args:
            l1, l2: given linked list

        Returns:
            linked list representing sum of two lists

        Time: O(n) - n = maximum of length of  l1 or l2
        Space: O(n)
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_sum = val1 + val2 + carry
            carry = curr_sum // 10
            digit = curr_sum % 10

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# 9.28 -> 9 min to solve