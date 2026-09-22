# 2.06

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if q is a subtree of p.

        Args:
            p, q (TreeNode): given binary trees

        Returns:
            bool: True if q is subtree of p else False

        Time: O(m*n) - m = total number of nodes in p tree, n = total number of nodes in q tree

        Space: O(h1 + h2) - h1, h2 = height of tree p and q
        """

        if not p:
            return False

        if not q:
            return True

        if self.same_tree(p, q):
            return True

        return self.is_subtree(p.left, q) or self.is_subtree(p.right, q)

    def same_tree(self, m: TreeNode, n: TreeNode) -> bool:
        """Find out if the given trees are same or not."""

        if not m and not n:
            return True

        if m and n and m.val == n.val:
            return self.same_tree(m.left, n.left) and self.same_tree(m.right, n.right)

        return False