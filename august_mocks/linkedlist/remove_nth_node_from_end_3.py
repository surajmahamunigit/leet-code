# 9.05

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Remove the nth node from the end of the given linked list.

        Args:
            head: head nod eof the given linked list
            n: nth node from end

        Returns:
            removes nth node from the end and returns head of the list

        Time: O(n) - n = length of linked list
        Space: O(1)
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

# 9.10 -> 5 min to finish
