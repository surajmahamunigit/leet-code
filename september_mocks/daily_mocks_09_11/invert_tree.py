# 7.09

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
            TreeNode: invert the given tree and return

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

# 7.15