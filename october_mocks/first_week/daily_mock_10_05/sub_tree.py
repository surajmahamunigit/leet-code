# 2.15

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_sub_tree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if tree q is subtree of tree p.

        Args:
            p (TreeNode): tree to look up
            q (TreeNode): subtree

        Returns:
            bool: True if q is subtree of p else False

        Time complexity: O(m*n) - m, n = total number of nodes in tree p and q

        Space complexity: O(h1+h2) - h1, h2 = height of tree p and q
        """

        if not q:
            return True

        if not p:
            return False

        if self.same_tree(p, q):
            return True

        return self.is_sub_tree(p.left, q) or self.is_sub_tree(p.right, q)


    def same_tree(self, m: TreeNode, n: TreeNode) -> bool:
        """Find out if the given trees are same."""

        if not m and not n:
            return True

        if not m or not n or m.val != n.val:
            return False

        return self.same_tree(m.left, n.left) and self.same_tree(m.right, n.right)
