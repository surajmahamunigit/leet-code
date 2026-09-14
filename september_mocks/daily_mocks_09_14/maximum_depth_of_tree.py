# 12.34

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthRecursive(self, root: TreeNode) -> int:
        """Find the maximum depth of the given tree.

        Args:
            root (TreeNode): The root node of the tree.

        Returns:
            int: The maximum depth of the given tree.

        Time: O(n) - n = total number of nodes in the tree.
        Space: O(h) - h = height of the given tree.
        """

        # base case
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

    def maxDepthIterative(self, root: TreeNode) -> int:
        """Find the maximum depth of the given tree.

        Args:
            root (TreeNode): The root node of the tree.

        Returns:
            int: The maximum depth of the given tree.

        Time: O(n) - n = total number of nodes in the tree.
        Space: O(h) - h = height of the given tree.
        """

        max_depth = 0
        stack = [[root, 1]]

        while stack:
            node, height = stack.pop()

            if node:
                max_depth = max(max_depth, height)

                stack.append([node.left, height+1])
                stack.append([node.right, height+1])

        return max_depth