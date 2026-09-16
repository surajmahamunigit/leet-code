# 10.25

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if the given trees are same or not.

        Args:
            p, q (TreeNode): given trees

        Returns:
            bool: True if the given trees are same, False otherwise

        Time: O(min(m,n)) - m, n = number of nodes in p and q

        Space: O(h) - h = minimum height of p and q
        """



        # 3 conditions
        # if both are None
        if not p and not q:
            return True

        # if one is None
        if not p or not q or p.val != q.val:
            return False

        # compare left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

