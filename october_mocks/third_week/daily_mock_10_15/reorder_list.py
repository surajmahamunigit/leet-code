# 6.41

# given -> linked list
# asked -> reorder it

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode|None) -> None:
        """Reorder the given linked list.

        Args:
            head (ListNode|None): given linked list

        Returns:
            None
        Time complexity: O(n) - n = total number of nodes in list

        Space complexity: O(1)
        """

        if head is None:
            return None

        # split the list
        slow = head
        fast = head.next
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

        # reorder two halfs
        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2

# 6.51 -> 10 minutes to solve problem
# git commit -> feat: add reorder list solution