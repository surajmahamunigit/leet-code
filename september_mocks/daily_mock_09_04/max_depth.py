# 1.37

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthRecursive(self, root: TreeNode) -> int:
        """Find the maximum depth of given binary tree.

        Args:
            root (TreeNode): root node of given binary tree

        Returns:
            int: maximum depth of given binary tree

        Time: O(n) - n = total number of nodes in given binary tree
        Space: O(h) - h = height of given binary tree
        """

        # base case
        if not root:
            return 0

        return 1 + max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right))


    def maxDepthIterative(self, root: TreeNode) -> int:
        """Find the maximum depth of given binary tree.

        Args:
            root (TreeNode): root node of given binary tree

        Returns:
            int: maximum depth of given binary tree

        Time: O(n) - n = total number of nodes in given binary tree
        Space: O(h) - h = height of given binary tree
        """

        max_depth = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)

                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return max_depth