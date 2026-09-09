# 8.42

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Invert the given binary tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            TreeNode: inverted binary tree

        Time: O(n) - n = number of nodes in given tree
        Space: O(h) - h = height of the given tree
        """

        # base case
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

