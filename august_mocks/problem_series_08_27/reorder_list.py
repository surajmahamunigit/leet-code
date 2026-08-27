# 4.41

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        """Reorder the given linked list.

        Args:
            head: head node of the given list

        Returns:
            reorder given list and return

        Time: O(n)
        Space: O(1)
        """

        # find middle
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

        # combine both halfs
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

# 4.48 -> 7 min to solve