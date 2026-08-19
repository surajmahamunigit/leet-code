# 11.56
# given list, asked to reorder it
# split it into two half -> reverse second halfs -> joint both halfs alternatively

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        """Reorder the given list and return.

        Args:
            head: head node of given list

        Returns:
            reorders lists and returns head node

        Time: O(n) - n = length of linked list
        Space: O(1)
        """
        # find middle
        left = head
        right = head.next
        while right and right.next:
            left = left.next
            right = right.next.next

        # reverse second half
        curr = left.next
        left.next = None
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # join both half alternatively
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

s = Solution()
def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

def build_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

s = Solution()
l1 = build_list([1,2,3,4])
s.reorderList(l1)
assert to_list(l1) == [1,4,2,3]

l2 = build_list([1,2,3,4,5])
s.reorderList(l2)
assert to_list(l2) == [1,5,2,4,3]

l3 = build_list([1])
s.reorderList(l3)
assert to_list(l3) == [1]

l4 = build_list([1,2])
s.reorderList(l4)
assert to_list(l4) == [1,2]

print("passed")




















