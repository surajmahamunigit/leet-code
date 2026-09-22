# 1.56
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if the given trees are same or not.

        Args:
            p, q (TreeNode): given binary trees

        Returns:
            bool: True if the trees are same, False otherwise

        Time: O(min(m, n)) - m, n = total number of nodes in p and q

        Space: O(min(h1, h2)) - h1, h2 = heights of tree p and q
        """

        # 3 conditions

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)

# 2.03 -> 7 min