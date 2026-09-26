# 7.25

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth_iterative(self, root: TreeNode) -> int:
        """Find maxim depth of the given binary tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            TreeNode: maximum depth of the binary tree

        Time: O(n) - n = total number of nodes in the tree

        Space: O(h) - h = height of tree
        """

        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return 1 + max(left, right)

    def max_depth_recursive(self, root: TreeNode) -> int:

        stack = [[root, 1]]
        max_depth = 0

        while stack:

            node, height = stack.pop()
            if node:
                max_dept = max(max_depth, height)

                stack.append([node.left, height + 1])
                stack.append([node.right, height + 1])

        return max_depth