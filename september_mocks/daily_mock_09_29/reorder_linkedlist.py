# 10.48

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder_linkedlist(self, head: ListNode) -> ListNode:
        """Reorder the given linkedlist.

        Args:
            head (ListNode): given linked list

        Returns:
            ListNode: reordered linked list

        Time complexity: O(n) - n = total number of nodes in given list

        Space complexity: O(1)
        """

        slow = head
        fast = head.next

        # find middle of linked list
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

        # join two halfs in alternative way
        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next if l1 else None
            temp2 = l2.next if l2 else None

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2

        return head

