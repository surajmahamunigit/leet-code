# 2.14

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """Reverse the given linked list and return new head.

        Args:
            head: head node of given linked list

        Returns:
            head node of reversed linked list

        Time: O(n) - n = number of nodes in given linked list
        Space: O(1)
        """

        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

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
assert to_list(s.reverseList(build_list([1,2,3,4,5]))) == [5,4,3,2,1]
assert to_list(s.reverseList(build_list([1,2]))) == [2,1]
assert to_list(s.reverseList(build_list([1]))) == [1]
assert to_list(s.reverseList(build_list([]))) == []
print("passed")