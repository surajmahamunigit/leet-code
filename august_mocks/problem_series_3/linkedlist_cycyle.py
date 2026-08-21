# 5.55
# given linked list and asked to detect if there is any cycle in linked list.
# use two pointers, left = head and right = head.next -> keep moving left and right for each right and right.next
# if they equal at any point -> return there is cycle
# else right will become None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """Detect if there is cycle in given linked list.

        Args:
            head: head node of the given list

        Returns:
            True if linked list has cycle, else False

        Time: O(n) - n = length of linked list
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
assert s.hasCycle(build_list([3,2,0,-4], 1)) == True
assert s.hasCycle(build_list([1,2], -1)) == False
assert s.hasCycle(build_list([1], -1)) == False
assert s.hasCycle(build_list([1], 0)) == True
assert s.hasCycle(None) == False

print("passed")

# 6.02 -> 7 min to solve