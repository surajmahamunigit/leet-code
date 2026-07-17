class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Invert the given tree.

        Args:
            root: root Node of the give tree

        Returns:
            inverted tree

        Time: O(n) - visits every node once
        Space: O(h) - h = height of tree
        """

        # step 1: base case
        if not root:
            return None

        # step 2: swap
        root.left, root.right = root.right, root.left

        # call inverseTree() on left and right Node because they are heads
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root