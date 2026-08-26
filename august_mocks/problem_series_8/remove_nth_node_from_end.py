# 8.44

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Remove the nth node from the end of the linked list and return head node.

        Args:
            head: head node of the given list
            n: number of nodes from the end of the list

        Returns:
            removes nth node from end and returns head of list

        Time: O(n) - n = length of list
        Space: O(1)
        """

        dummy = ListNode(val=0, next=head)
        left = dummy
        right = head

        # move right n nodes ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # move both
        while right:
            left = left.next
            right = right.next

        # remove nth node
        left.next = left.next.next

        return dummy.next

# 8.55 -> 11 min to solve