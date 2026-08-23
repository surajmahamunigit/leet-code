# 1.13
# given two numbers in form of reverse order as linked list and asked to return result in reverse order
# add two digits and carry -> find out carry and digit -> create new node for digit and attach it to current dummy node
# move current forward and move nodes of both list forward

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add given two numbers and return result in reverse as linked list.

        Args:
            l1, l2: given two number in reverse as linked lists

        Returns:
             result: linked list in reverse as linked list

        Time: O(m+n) - m, n = lengths of l1 and l2
        Space: O(1)
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

# 1.23 -> 10 min to solve