
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:

        # step 1: find the middle of the list
        slow = head
        fast = head.next  # for balanced half split

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Note: slow.next node now represents starting node of second half

        # step 2: reverse second half
        cur = slow.next  # starting node of 2nd half
        slow.next = None  # first half points to None
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # step 3: now we know starting Node of both half  [1, 2, 3] [6, 5, 4]
        first = head  # starting of first half [1]
        second = prev  # starting of second half [6]

        while second:
            # find next nodes
            temp1 = first.next
            temp2 = second.next

            first.next = second  # [1] -> [6]
            second.next = temp1  # [1] -> [6] -> [2]

            # move forward
            first = temp1  # [2]
            second = temp2  # [5]


