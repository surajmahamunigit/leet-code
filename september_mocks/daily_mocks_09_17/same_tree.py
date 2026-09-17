# 4.44

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find if given two trees are same or not.

        Args:
            p, q (TreeNode): given binary trees

        Returns:
            bool: True if given two trees are same, else False

        Time: O(min(m,n)) - m, n = number of nodes in p and q

        Space: O(min(h1, h2)) - h1, h2 = height tree p and q
        """

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)