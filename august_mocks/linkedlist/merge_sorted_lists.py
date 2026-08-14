# 6.39

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted list in sorted order and return head of new list.

        Args:
            l1: head node of first sorted list
            l2: head node of second sorted list

        Returns:
            head node of merged sorted list

        Time: O(m + n) - m, n = lengths of list l1 and l2
        Space: O(1)
        """

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next

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
assert to_list(s.mergeTwoLists(build_list([1,2,4]), build_list([1,3,4]))) == [1,1,2,3,4,4]
assert to_list(s.mergeTwoLists(build_list([]), build_list([]))) == []
assert to_list(s.mergeTwoLists(build_list([]), build_list([0]))) == [0]
assert to_list(s.mergeTwoLists(build_list([1,2,3]), build_list([]))) == [1,2,3]
print("passed")

# 6.47 -> 11 min to solve