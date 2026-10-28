# 12.24

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node(self, head: ListNode|None, n: int) -> ListNode|None:
        """Remove the nth node from end of the given list.

        Args:
            head (ListNode|None): head node of the given list
            n: position of node to be removed from the end of the given list

        Returns:
            ListNode|None: head node of list after removing nth node from end

        Time complexity: O(L) - L = total number of nodes in the list

        Space complexity: O(1)
        """

        if not head:
            return None

        dummy = ListNode(next=head)
        slow = dummy
        fast = head

        # move fast n nodes ahead of head
        while fast and n > 0:
            fast = fast.next
            n -= 1

        # move slow and fast
        while fast:
            slow = slow.next
            fast = fast.next

        # remove nth node
        slow.next = slow.next.next

        return dummy.next

# 12.37 -> 13 minutes to solve problem and write test cases
# git commit -> feat: add remove nth node from end solution

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

def check(values, n, expected):
    result = s.remove_nth_node(build_list(values), n)
    assert list_to_values(result) == expected

check([1], 1, [])
check([1,2], 1, [1])
check([1,2], 2, [2])
check([1,2,3], 1, [1,2,])
check([], 0, [])
check([1,2,3,4,5], 5, [2,3,4,5])

print("all passed")