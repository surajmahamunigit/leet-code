# 11.08
# given -> two list representing numbers in reverse order
# asked -> add two numbers and return result in same format

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers given as linked list and return result.

        Args:
            l1, l2 (ListNode): given numbers as linked list in reverse order

        Returns:
            ListNode: head node of list representing addition of two numbers in reverse order

        Time complexity: O(max(n1, n2)) - n1, n2 = total number of nodes in l1 and l2

        Space complexity: O(max(n1, n2))
        """

        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_sum = val1 + val2 + carry
            carry = curr_sum // 10
            digit = curr_sum % 10

            node = ListNode(val=digit)
            curr.next = node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# 11.18 -> 10 minute sto finish problem
# git commit -> feat: add add two numbers solution
