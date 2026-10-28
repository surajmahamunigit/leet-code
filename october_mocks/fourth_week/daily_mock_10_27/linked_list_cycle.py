# 10.20

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def has_cycle(self, head: ListNode|None) -> bool:
        """Find out if the given list has cycle.

        Args:
            head (ListNode): head node of the given list

        Returns:
            bool: True if the given list has cycle, else False

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(1)
        """

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

# 10.25 -> 5 minutes to solve problem
# git commit -> feat: add linkedlist cycle detection solution

def build_list(values, pos):
    dummy = ListNode()
    tail = dummy
    cycle_start = None

    for index, val in enumerate(values):
        tail.next = ListNode(val=val)
        tail = tail.next

        if index == pos:
            cycle_start = tail

    tail.next = cycle_start
    return dummy.next

s = Solution()

def check(values, expected, pos=-1 ):
    result = s.has_cycle(build_list(values, pos))
    assert result == expected

check(values=[1,2,3,4],expected=False)
check(values=[1], expected=False)
check(values=[1], expected=True, pos=0)
check(values=[1,2], expected=True, pos=0)
check(values=[1,2], expected=False)
print("all passed")

