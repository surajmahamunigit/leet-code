class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find oout if trees are same or not.

        Args:
            p: root of first tree
            q: root of second tree

        Returns:
            True if trees are same, else False

        Time: O(m + n) - m and n = length of firs and second tree
        Space:O(h1 + h2) - h1, h2 = height of first and second tree
        """

        # step 1: if both are None
        if not p and not q:
            return True                 # None = same

        # step 2: what if only one is None
        #       : what if both have different values
        if not p or not q or p.val != q.val:
            return False

        # step 3: call isSameTree() on left and right node
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))