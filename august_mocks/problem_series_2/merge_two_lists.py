# 12.34
# given two sorted linked lists l1, l2 and asked to merge them in sorted order
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge the given two lists in sorted order.

        Args:
            l1, l2: given sorted lists head nodes

        Returns:
            merges two lists in sorted order and returns head

        Time: O(m+n) - m,n = length of both lists
        Space: O(1)
        """

        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 <= val2:
                curr.next = l1
                l1 = l1.next        # move left
                curr = curr.next    # move current pointer
            else:
                curr.next = l2
                l2 = l2.next        # move l2
                curr = curr.next    # move current pointer

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

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

# 12.47 -> 13 min to solve