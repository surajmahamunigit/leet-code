# 1.55

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if the given trees are same.

        Args:
            p, q (TreeNode): given binary trees

        Returns:
            bool: True if the trees are same, False otherwise

        Time complexity: O(min(m, n)) - m, n are total number of nodes in tree

        Space complexity: O(min(h1, h2)) - h1, h2 = height of given trees
        """

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)