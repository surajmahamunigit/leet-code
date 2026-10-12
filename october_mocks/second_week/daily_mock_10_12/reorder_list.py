# 12.21
from typing import Optional


# given linked list
# asked to to reorder it

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]):
        """Reorder the given linked list.

        Args:
            head (ListNode): head node of the given linkedlist

        Returns:
            None: the list is reordered in place

        Time complexity: O(n) - n = number of nodes in the list

        Space complexity: O(1)
        """

        if head is None:
            return

        slow = head
        fast = head.next

        # find middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        prev = None
        curr = slow.next
        slow.next = None

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



# 12.29 -> 8 minutes to solve problem
# git commit -> feat: add reorder list solution

def build(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head):
    out = []
    while head and len(out) < 10**6:
        out.append(head.val)
        head = head.next
    return out

s = Solution()
h = build([1, 2, 3, 4]); assert s.reorderList(h) is None; assert to_list(h) == [1, 4, 2, 3]
h = build([1, 2, 3, 4, 5]); s.reorderList(h); assert to_list(h) == [1, 5, 2, 4, 3]
h = build([1]); s.reorderList(h); assert to_list(h) == [1]
h = build([1, 2]); s.reorderList(h); assert to_list(h) == [1, 2]
h = build([1, 2, 3]); s.reorderList(h); assert to_list(h) == [1, 3, 2]
h = build([1, 2, 3, 4, 5, 6]); s.reorderList(h); assert to_list(h) == [1, 6, 2, 5, 3, 4]
h = build([1, 2, 3, 4, 5, 6, 7]); s.reorderList(h); assert to_list(h) == [1, 7, 2, 6, 3, 5, 4]
h = build([5, 5, 5, 5]); s.reorderList(h); assert to_list(h) == [5, 5, 5, 5]
h = build([10, 20, 30, 40, 50, 60, 70, 80]); s.reorderList(h); assert to_list(h) == [10, 80, 20, 70, 30, 60, 40, 50]
n = 100000
h = build(list(range(n))); s.reorderList(h)
exp = []
for i in range(n // 2):
    exp += [i, n - 1 - i]
assert to_list(h) == exp