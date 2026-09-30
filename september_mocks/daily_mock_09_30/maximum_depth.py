# 10.30
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximum_depth(self, root: TreeNode) -> int:
        """Find the maximum depth of the given tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            int: maximum depth of the binary tree

        Time complexity: O(n) - n = total number of nodes in given tree

        Space complexity: O(h) - h = height of the given tree
        """

        if not root:
            return 0

        left = self.maximum_depth(root.left)
        right = self.maximum_depth(root.right)

        return max(left, right) + 1