# 11.56
# given head node of linked list and asked to remove nth node from end of linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Remove nth node from end of list and return list.

        Args:
            head: head node of given list
            n: node to remove from end of linked list

        Returns:
            removes nth node from end of list and returns list

        Time: O(n) - n = length of linked list
        Space: O(1)
        """
        dummy = ListNode(val=0, next=head)
        left = dummy
        right = head

        while n > 0 and right :
            right = right.next
            n -= 1

        # now move both pointers one at a time
        while right:
            left = left.next
            right = right.next

        # replace nth node
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
assert to_list(s.removeNthFromEnd(build_list([1,2]), 2)) == [2]
assert to_list(s.removeNthFromEnd(build_list([1,2,3,4,5]), 5)) == [2,3,4,5]
print("passed")

# 12.06 -> 10 min to solve