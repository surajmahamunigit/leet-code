# 8.40

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode|None, l2: ListNode) -> ListNode|None:
        """Add the given two numbers given as linked list in reverse order.

        Args:
            l1: first number
            l2: second number

        Returns:
            ListNode|None: head node of the result of addition of two numbers

        Time complexity: O(n1+n2) - n1, n2 = total number of nodes in list l1 and l2

        Space complexity: O(max(n1, n2))
        """

        dummy = ListNode()
        tail = dummy
        carry = 0
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

def build_list(values):
    dummy = ListNode()
    tail = dummy
    for val in values:
        tail.next = ListNode(val=val)
        tail = tail.next

    return dummy.next

def list_to_values(head, limit=100_000):
    out = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next

    return out

s = Solution()

def check(values1, values2, expected):
    result = s.add_two_numbers(build_list(values1), build_list(values2))
    assert list_to_values(result) == expected

check([1], [2], [3])
check([1],[], [1])
check([1,2], [3], [4,2])
check([1,2], [9], [0,3])
check([1,2,3], [4,5,6], [5,7,9])
print("all passed")