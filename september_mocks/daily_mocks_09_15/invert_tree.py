# 11.28

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
            TreeNode: the inverted tree.

        Time: O(n) - n = total number of nodes in the tree.
        Space: O(h) - = height of the given tree
        """

         # base condition
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root