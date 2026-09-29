# 4.04

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node(self, head: ListNode, n: int) -> ListNode:
        """Remove the nth node from the end of the list.

        Args:
            head (ListNode): given linked list
            n (int): nth node to remove from the end of the list

        Returns:
            ListNode: removes nth node from the end of the list and return

        Time complexity: O(n) - n = total number of nodes in linked list

        Space complexity: O(1)
        """

        dummy = ListNode(next=head)
        slow = dummy
        fast = head

        # move fast n nodes ahead of slow node
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        # move slow and fast pointers
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next