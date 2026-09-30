# 12.15

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if given trees are same or not.

        Args:
            p, q (TreeNode): given binary trees

        Returns:
            bool: True if trees are same, else False

        Time complexity: O(min(m, n)) - m, n = total number of nodes in p and q

        Space complexity: O(min(h1, h2)) - h1, h2 = height of p and q
        """

        # if both are not there
        if not p and not q:
            return True

        # if one is None
        if not p or not q or p.val != q.val:
            return False

        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)