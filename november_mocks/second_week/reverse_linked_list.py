# 9.50

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: ListNode|None) -> ListNode|None:
        """Reverse the given linked list.

        Args:
            head: head node of the given linked list
        Returns:
            ListNode|None: head node of the given linked list
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

s = Solution()

def build_list(values):
    dummy = ListNode()
    tail = dummy

    for val in values:
        tail.next = ListNode(val=val)
        tail = tail.next

    return dummy.next

def list_to_values(head, limit=100_000):
    result = []
    curr = head

    while curr:

        if len(result) >= limit:
            raise AssertionError("Traversal limit reached")

        result.append(curr.val)
        curr = curr.next

    return result

def check(values, expected):
    result = s.reverse_list(build_list(values))
    assert list_to_values(result) == expected

check([], [])
check([1], [1])
check([1,2,3], [3,2,1])
check([8,3,2,5], [5,2,3,8])
print("all tests passed")