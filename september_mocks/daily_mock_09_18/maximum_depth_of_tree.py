# 12.44

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthRecursive(self, root: TreeNode) -> int:
        """Find the maximum depth of the tree.

        Args:
            root (TreeNode): given tree

        Returns:
            int: maximum depth of the tree

        Time: O(n) - n = total number of nodes in given tree

        Space: O(h) - h = height of given tree
        """

        # base case
        if not root:
            return 0

        left = self.maxDepthRecursive(root.left)
        right = self.maxDepthRecursive(root.right)

        return max(left, right) + 1

    def maxDepthIterative(self, root: TreeNode) -> int:

        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, height = stack.pop()

            if node:
                max_depth = max(max_depth, height)

                stack.append([node.left, height + 1])
                stack.append([node.right, height + 1])

        return max_depth