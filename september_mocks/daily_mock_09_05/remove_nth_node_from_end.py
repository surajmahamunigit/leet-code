# 6.07

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Remove the nth node from end of the given linkedlist.

        Args:
            head (ListNode): head node of the given linked list
            n (int): node to remove from the end of the list

        Returns:
             ListNode: remove the nth node from end and return the head of linked list

        Time: O(n) - n = total number of nodes in the list
        Space: O(1)
        """

        dummy = ListNode(next=head)

        slow = dummy
        fast = head

        # move fast pointer n nodes forward
        while fast and n>0:
            fast = fast.next
            n -= 1

        # move both nodes forward
        while fast:
            slow = slow.next
            fast = fast.next

        # remove nth node
        slow.next = slow.next.next

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
print('passed')