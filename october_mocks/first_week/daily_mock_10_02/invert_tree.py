# 2.13

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        """Invert the given tree.

        Args:
            root (reeNode): given binary tree

        Returns:
            TreeNode: inverted binary tree

        Time complexity: O(n) - n = total number of nodes in given tree

        Space complexity: O(h) - h = height of the given tree
        """

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root