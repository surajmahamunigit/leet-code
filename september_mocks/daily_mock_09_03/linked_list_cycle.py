# 6.42

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) ->bool:
        """Find out if the given linked list has cycle.

        Args:
            head (ListNode): headnode of the given list

        Returns:
            True if the given linked list has cycle, else False

        Time: O(n) - n = total number of nodes in given linked list
        Space: O(1)
        """

        if head == None:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True

        return False



def build_list(values, pos):
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None

s = Solution()
assert s.hasCycle(build_list([3,2,0,-4], 1)) == True
assert s.hasCycle(build_list([1,2], -1)) == False
assert s.hasCycle(build_list([1], -1)) == False
assert s.hasCycle(build_list([1], 0)) == True
assert s.hasCycle(None) == False
print('passed')