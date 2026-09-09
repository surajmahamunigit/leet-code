# 12.44

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Find the two numbers as linked list in reverse order and return result in same format.

        Args:
            l1, l2 (ListNode): given two numbers as linked list in reverse order

        Returns:
            ListNode: result as linked list in reverse order

        Time: O(m) - m = maximum of total number of nodes in l1 and l2
        Space: O(m)
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

            new_node = ListNode(val=digit)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# 12.50 -> 6 min