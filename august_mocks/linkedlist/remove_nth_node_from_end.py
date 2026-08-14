# 8.50

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Remove the nth node from the end of the linked list and return head.

        Args:
            head: head node of the given linked list

        Returns:
            removes nth node from end and returns lists

        Time: O(n) - n = length of linked list
        Space: O(1)
        """
        # [1,2,3,4,5]), 2
        dummy = ListNode(0, head)
        left = dummy
        right = head
        count = 0
        while right and count < n:
            right = right.next
            count += 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

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
assert to_list(s.removeNthFromEnd(build_list([1,2,3,4,5]), 2)) == [1,2,3,5]
assert to_list(s.removeNthFromEnd(build_list([1]), 1)) == []
assert to_list(s.removeNthFromEnd(build_list([1,2]), 1)) == [1]
assert to_list(s.removeNthFromEnd(build_list([1,2]), 2)) == [2]      # removing the head
assert to_list(s.removeNthFromEnd(build_list([1,2,3,4,5]), 5)) == [2,3,4,5]  # n = full length
print("passed")