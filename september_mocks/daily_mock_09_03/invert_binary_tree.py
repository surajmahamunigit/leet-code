# 7.20

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Invert the given tree.

        Args:
            root (TreeNode): root of the tree.

        Returns:
            TreeNode: inversion of the given tree.

        Time: O(n) - n = total number of nodes in given binary tree
        Space: O(1)
        """

        # base case
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# 7.24 -> 4 min