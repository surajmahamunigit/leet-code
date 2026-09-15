# 11.22

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthRecursive(self, root: TreeNode) -> int:
        """Find the maximum depth of the binary tree.

        Args:
            root (TreeNode): The root of the tree.

        Returns:
            int: The maximum depth of the tree.

        Time: O(n) - n = number of nodes in the tree.
        Space: O(h) - h = height of the given tree.
        """

        # base condition
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

    def maxDepthIterative(self, root: TreeNode) -> int:
        """Find the maximum depth of the binary tree.

        Args:
            root (TreeNode): The root of the tree.

        Returns:
            int: The maximum depth of the tree.

        Time: O(n) - n = number of nodes in the tree.
        Space: O(h) - h = height of the given tree.
        """

        max_depth = 0
        stack = [[root, 1]]

        while stack:
            node, height = stack.pop()

            if node:
                max_depth = max(max_depth, height)

                stack.append([node.left, height + 1])
                stack.append([node.right, height + 1])
        return max_depth