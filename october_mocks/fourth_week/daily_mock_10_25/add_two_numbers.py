# 10.38

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two given numbers in forms in reverse linked list form.

        Args:
            l1 (ListNode): first number
            l2 (ListNode): second number

        Returns:
              ListNode: addition of given two numbers in reverse order linked list

        Time complexity: O(max(n1, n2)) - n1, n2 = total number of nodes in l1 and l2

        Space complexity: O(max(n1, n2))
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

        return dummy.next

s = Solution()
def check(values1, values2, expected):
    result = s.addTwoNumbers(build_list(values1), build_list(values2))
    assert list_to_values(result) == expected

def build_list(values):
    dummy = ListNode()
    tail = dummy

    for val in values:
        tail.next = ListNode(val=val)
        tail = tail.next

    return dummy.next

def list_to_values(head, limit=100_000):
    out = []

    while head and len(out) <= limit:
        out.append(head.val)
        head = head.next

    return out

# 10.54 -> total tastes and code writing time 16 minutes
# git commit -> feat: add add two numbers solution

check([1,2,3], [5,6,3], [6, 8, 6])
check([2,4,3], [5,6,4], [7,0,8])
#check([0],[0], [0])
check([1,2], [6,5,4], [7,7,4])
print("all passed")