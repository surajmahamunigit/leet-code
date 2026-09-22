# 7.01

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        """Invert the given tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            TreeNode: inverted binary tree

        Time: O(n) - n = number of nodes in given binary tree

        Space: O(h) - h = height of the given tree
        """

        # base case
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root