# 11

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two given lists and return head or result.

        Args:
            l1, l2: head nodes of given linked lists

        Returns:
            head node after adding two lists

        Time: O(n) - n = max length between two lists
        Space: O(n+1) = O(n)
        """

        dummy = ListNode()
        curr = dummy
        carry = 0
        first = l1
        second = l2

        while first or second or carry:
            val1 = first.val if first else 0
            val2 = second.val if second else 0
            curr_sum = carry + val1 + val2

            carry = curr_sum // 10
            digit = curr_sum % 10

            new_node = ListNode(digit)
            curr.next = new_node
            curr = new_node

            first = first.next if first else None
            second = second.next if second else None

        return dummy.next

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
assert to_list(s.addTwoNumbers(build_list([2,4,3]), build_list([5,6,4]))) == [7,0,8]        # 342 + 465 = 807
assert to_list(s.addTwoNumbers(build_list([0]), build_list([0]))) == [0]
assert to_list(s.addTwoNumbers(build_list([9,9,9]), build_list([1]))) == [0,0,0,1]           # carry produces an extra digit
assert to_list(s.addTwoNumbers(build_list([9,9]), build_list([9,9,9]))) == [8,9,0,1]         # different lengths + carry
print("passed")

# 11.40 -> 40 minutes to finish