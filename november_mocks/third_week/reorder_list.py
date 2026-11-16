# 7.34

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder_list(self, head: ListNode) -> ListNode:
        """Reorder the given list.

        Args:
            head: head node of the given list

        Returns:
            ListNode: head node of the reordered list

        Time complexity: O(n) - n = number of nodes in the list

        Space complexity: O(1)
        """
        # [1,2,3,5,7]

        if head is None:
            return None

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # revers the second half of the list
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # joint two half
        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2

        return head


