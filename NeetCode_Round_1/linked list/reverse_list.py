class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Args:
            head: start node of list

        Returns:
            reversed list

        Time:
        Space:
        """

        prev = None
        cur = head

        while cur:

            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev