# 7.15
# given -> linkedlist
# asked -> find if list has cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode|None) -> bool:
        """Find out if the given list has cycle.

        Args:
            head (ListNode|None): head node of the given list

        Returns:
            bool: True if the list has a cycle, else False

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(1)
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# 7.20 -> 5 minutes to finish problem
# git commit -> feat: add linked list cycle solution
s = Solution()
a, b, c = ListNode(1), ListNode(2), ListNode(3)
a.next = b
b.next = c
c.next = b
assert s.hasCycle(a) == True

c.next = None
assert s.hasCycle(a) == False
print('all passed')