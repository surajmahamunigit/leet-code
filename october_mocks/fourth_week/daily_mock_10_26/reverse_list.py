# 2.39

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: ListNode|None) -> ListNode|None:
        """Reverse the given list.

        Args:
            head (ListNode|None): head node of the given list

        Returns:
            ListNode|None: head node of the inverted tree

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(1)
        """
        if not head:
            return None

        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# 2.48 -> 9 minute sto write all code
# git commit -> feat: add invert binary tree solution

s = Solution()

def check(values, expected):
    result = s.reverse_list(build_list(values))
    assert list_to_values(result) == expected

def build_list(values):
    dummy = ListNode()
    tail = dummy

    for val in values:
        tail.next = ListNode(val=val)
        tail = tail.next

    return dummy.next

def list_to_values(head, limit=100_00):
    out = []

    while head and len(out) <= limit:
        out.append(head.val)
        head = head.next

    return out

check([1,2,3,4], [4,3,2,1])
check([1], [1])
check([],[])
check([1,2], [2,1])
print("all passed")