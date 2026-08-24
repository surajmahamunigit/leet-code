# 11.29
# we are given head of linked list and asked to reorder it
# first find half of list. split and make two lists. for second half, reverse it. then combine 1st and 2nd list node by node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        """Reorder the given linked list.

        Args:
            head: head node of given linked list

        Returns:
            reordered list

        Time: O()
        Space: O()
        """


        # find half
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

        # combine both
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

# 11.40 -> 11 min to solve