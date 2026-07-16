class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Args:
            head staring node of a given list

        Returns:
            None

        Time:O(n)
        Space:O(1)
        """

        # step 1: find middle node of the list
        slow = head
        fast = head.next        # always returns first middle

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: find second half and reverse the order
        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # step 3: join two lists alternatively
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
