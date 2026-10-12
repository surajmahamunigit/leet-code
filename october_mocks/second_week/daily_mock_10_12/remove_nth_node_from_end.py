# 11.56

# given -> linked list
# asked to remove nth node from end


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Find and remove the nth node from end of the list.

        Args:
            head (ListNode): head node of the given linked list
            n (int): node to remove from end of the list

        Returns:
            ListNode: remove nth node from end of list and return head

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(1)
        """

        dummy = ListNode(next=head)
        left = dummy
        right = head

        # move the right pointers n nodes ahead of dummy
        while n > 0 and right:
            right = right.next
            n -= 1

        # move both left and right pointer till right reached None
        while right:
            left = left.next
            right = right.next

        # remove nth node from end
        left.next = left.next.next

        return dummy.next

# 12.06 -> 10 minute sto solve problem
# git commit -> feat: add remove nth node from end of list

def build(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

s = Solution()
assert to_list(s.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
assert to_list(s.removeNthFromEnd(build([1]), 1)) == []
assert to_list(s.removeNthFromEnd(build([1, 2]), 1)) == [1]
assert to_list(s.removeNthFromEnd(build([1, 2]), 2)) == [2]
assert to_list(s.removeNthFromEnd(build([1, 2, 3]), 3)) == [2, 3]
assert to_list(s.removeNthFromEnd(build([1, 2, 3]), 1)) == [1, 2]
assert to_list(s.removeNthFromEnd(build([1, 2, 3]), 2)) == [1, 3]
assert to_list(s.removeNthFromEnd(build([1, 1, 1, 1]), 2)) == [1, 1, 1]
assert to_list(s.removeNthFromEnd(build([1, 1]), 2)) == [1]
assert to_list(s.removeNthFromEnd(build(list(range(1, 11))), 10)) == list(range(2, 11))
assert to_list(s.removeNthFromEnd(build(list(range(1, 11))), 1)) == list(range(1, 10))
big = to_list(s.removeNthFromEnd(build(list(range(100000))), 50000))
assert big == list(range(50000)) + list(range(50001, 100000))