class TreeNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: TreeNode) -> bool:

        slow = head         # pointer
        fast = head         # pointer

        # if at any point slow == fast, there is cycle in linkedlist
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False