# 11.42

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder_list(self, head: ListNode) -> None:
        """Reorder the linkedlist.

        Args:
            head (ListNode): given linkedlist

        Returns:
            None

        Time: O(n) - n = total number of nodes in given list

        Space: O(1)
        """

        slow = head
        fast = head.next

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # join two halfs
        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2

