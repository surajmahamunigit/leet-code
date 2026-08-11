# algorithm
# given head node of the current array and asked to check if there is cycle meaning
# lets assume left = head, right = head
# while right -> left = left.next, right = right.next.next -> if left node == right node return False
# in end return -1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def cycle_in_linkedlist(self, head: ListNode) -> bool:
        """Find if there is cycle or not.

        Args:
            head: head node of given list

        Returns:
            True if there is cycle in list else False

        Time: O(n) - n = length of list because right catches left with n steps
        Space: O(1)
        """
        left = head
        right = head
        while right and right.next:      # check both right and right.next otherwise we will get AttributeError
            left = left.next
            right = right.next.next

            if left == right:
                return True

        return False