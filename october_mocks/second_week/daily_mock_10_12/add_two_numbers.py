# 1.10

#given -> two numbers in reverse order as linked list
# asked -> add these two numbers and return result in reverse order

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers given as reverse linked list and return result in same format.

        Args:
            l1, l2 (ListNode): given linked lists representing two numbers in reverse order

        Returns:
            ListNode: result of sum of two numbers in reverse order as linked list

        Time complexity: O(max(n1, n2)) - n1, n2 = total number of nodes in l1 and l2 lists

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
            new_node = ListNode(val=digit)

            curr.next = new_node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# 1.16 -> 6 minutes to solve the problem
# git commit -> feat: add add two numbers solution

