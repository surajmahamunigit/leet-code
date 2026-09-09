# 10.53

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if the given tress are same or not.

        Args:
            p, q (TreeNode): given binary trees

        Returns:
            bool: True if the given tress are same, False otherwise

        Time: O(n) - n = number of nodes in given tree
        Space: O(h) - h = height of the given tree
        """

        # if both nodes are empty
        if not p and not q:
            return True

        # if exactly one is empty
        if not p or not q:
            return False

        # if values dont match
        if p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)