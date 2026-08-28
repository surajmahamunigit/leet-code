# 9.18

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Invert the given binary tree.

        Args:
            root: root node of the given binary tree

        Returns:
            inverted binary tree

        Time: O(n) - n = total number of nodes in tree
        Space: O(h) - h = height of binary tree
        """

        # base case
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# 9.22 -> 4 min to solve