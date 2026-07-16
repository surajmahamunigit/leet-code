class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Remove nth node from the end of the list.

        Args:
            head: starting Node of the list
            n: node to be removed

        Returns:
            head of list with nth node from end removed

        Time: O(m) - m = length of list
        Space: O(1)
        """

        # step 1: create a dummy node
        dummy = ListNode(0, head)       # val = 0, next = head

        left = dummy
        right = head

        # step 2: create n-node gap between left and right
        while n > 0 and right:
            right = right + 1
            n = n - 1

        # step 3: move right and left till right = None
        while right:
            left = left.next
            right = right.next

        # step 4: remove nth node
        left.next = left.next.next      # skip next node of left poiter node

        return dummy.next