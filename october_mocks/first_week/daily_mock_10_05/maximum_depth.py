# 12.31

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximum_depth_recursive(self, root: TreeNode) -> int:
        """Find the maximum depth of the given binary tree.

        Args:
            root (TreeNode): root node of the given tree.

        Returns:
            int: maximum depth of the given binary tree.

        Time complexity: O(n) - n = total number of nodes in given tree

        Space complexity: O(h) - h = height of the given tree
        """

        if not root:
            return 0

        left = self.maximum_depth_recursive(root.left)
        right = self.maximum_depth_recursive(root.right)

        return 1 + max(left, right)

    def maximum_depth_iterative(self, root: TreeNode) -> int:
        """Find the maximum depth of the given binary tree.

        Args:
            root (TreeNode): root node of the given tree.

        Returns:
            int: maximum depth of the given binary tree.

        Time complexity: O(n) - n = total number of nodes in given tree

        Space complexity: O(h) - h = height of the given tree
        """

        stack = [[root, 1]]
        max_height = 0
        while stack:
            node, height = stack.pop()

            if node:
                max_height = max(max_height, height)

                stack.append([node.left, height + 1])
                stack.append([node.right, height + 1])

        return max_height