# 6.36

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Node) -> None:
        """Reorder the given linked list.

        Args:
            head: head node of given linked list

        Returns:
            Reorders the given list

        Time: O(n) - n = length of linked list
        Space: O(1)
        """

        left = head
        right = head.next
        while right and right.next:
            left = left.next
            right = right.next.next


        curr = left.next
        prev = None
        left.next = prev
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        return head

# 6.44 -> 8 min to finish