# 11.35

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """Determine if the given linkedlist has cycle in it.

        Args:
            head: head node of given linkedlist

        Returns:
            True if linkedlist has cycle, else False

        Time: O(n) - fast will take less n steps to catch slow if there is cycle.
        Space: O(1)
        """

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
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
assert s.hasCycle(build_list([3,2,0,-4], 1)) == True    # cycle back to index 1
assert s.hasCycle(build_list([1,2], -1)) == False        # no cycle
assert s.hasCycle(build_list([1], -1)) == False           # single node, no cycle
assert s.hasCycle(build_list([1], 0)) == True              # single node pointing to itself
assert s.hasCycle(None) == False                           # empty list
print("passed")

# 11.41 -> 6 min to finish