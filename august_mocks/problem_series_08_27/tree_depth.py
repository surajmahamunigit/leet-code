# 9.27
from logging import root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Find the maximum depth of binary tree.

        Args:
            root: root node of the binary tree

        Returns:
            max depth of the binary tree

        Time: O(n) - n = number of nodes in tree
        Space: O(h) - h = height of tree
        """
        # iterative approach
        stack = [[root, 1]]
        result = 0

        while stack:

            stack_node, stack_depth = stack.pop()
            if stack_node:
                result = max(result, stack_depth)
                stack.append([stack_node.left, stack_depth + 1])
                stack.append([stack_node.right, stack_depth + 1])

        return result


# 9.39 -> 12 min to solve

        # recursive approach

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))