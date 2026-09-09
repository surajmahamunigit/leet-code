# 8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add given two numbers and return result in same form.

        Args:
            l1, l2 (ListNode): given two linked lists representing number in reverse order

        Returns:
            ListNode: result of addition in reverse order

        Time: O(n) - n = maximum of number of nodes in l1 and l2
        Space: O(n)
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

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

s = Solution()
def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

def build_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

s = Solution()
assert to_list(s.addTwoNumbers(build_list([2,4,3]), build_list([5,6,4]))) == [7,0,8]
assert to_list(s.addTwoNumbers(build_list([0]), build_list([0]))) == [0]
assert to_list(s.addTwoNumbers(build_list([9,9,9]), build_list([1]))) == [0,0,0,1]
assert to_list(s.addTwoNumbers(build_list([9,9]), build_list([9,9,9]))) == [8,9,0,1]
print('passed')

# 8.08 -> 8 min