# 7.10

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximum_depth_recursive(self, root: TreeNode) -> int:
        """Find the maximum depth of the binary tree.

        Args:
            root (TreeNode): A binary tree node.

        Returns:
            int: The maximum depth of the tree.

        Time O(n) - n = total number of nodes in the tree.

        Space: O(h) - h = height of the given tree.
        """

        # base case
        if not root:
            return 0

        left = self.maximum_depth_recursive(root.left)
        right = self.maximum_depth_recursive(root.right)

        return 1 + max(left, right)

    def maximum_depth_iterative(self, root: TreeNode) -> int:
        """Find the maximum depth of the binary tree."""

        max_depth = 0
        stack = [[root, 1]]
        while stack:
            node, height = stack.pop()
            if node:
                max_depth = max(max_depth, height)

                stack.append([node.left, height+1])
                stack.append([node.right, height+1])

        return max_depth