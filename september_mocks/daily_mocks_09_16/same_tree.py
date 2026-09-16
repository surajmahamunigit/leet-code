# 11.33

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if given two trees are same or not.

        Args:
            p, q (TreeNode): given binary trees.

        Returns:
            bool: True if given trees are same, False otherwise.

        Time: O(min(p, q)) - p, q = total number of nodes in both trees.

        Space: O(min(m, n)) - m, n = height of the given trees.
        """

        # 3 conditions
        # if both are None
        if not p and not q:
            return True

        # if one is None r values are not same
        if not p or not q or p.val != q.val:
            return False

        # check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)