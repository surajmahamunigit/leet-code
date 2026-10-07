# 9.29

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge given sorted linked lists in sorted order.

        Args:
            l1, l2 (ListNode): head nodes of linked lists sorted in ascending order

        Returns:
            ListNode: head node of the merged sorted linked list

        Time complexity: O(n1 + n2) - n1, n2 = total number of nodes in l1 and l2

        Space complexity: O(1)
        """
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 <= val2:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next

# 9.37 ->8 minutes to solve the problem
# git commit suggestion -> feat: add merge two sorted linked lists into sorted list solution