# 9.23

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Find the maximum depth of given tree.

        Args:
            root (TreeNode): root node of given tree.

        Returns:
            int: maximum depth of given tree.

        Time: O(n) - n = number of nodes in given tree

        Space: O(h) - h = height of the given tree
        """

        # base case
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)