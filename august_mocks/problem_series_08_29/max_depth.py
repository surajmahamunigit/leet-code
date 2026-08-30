# 2.21

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Find the maximum depth of the given binary tree.

        Args:
            root: given binary tree

        Returns:
            max depth of iven binary tree

        Time: O(n) - n = number of nodes in binary tree
        Space: O(h) - h = height binary tree

        """

        # Approach 1: recursive approach

        # base case
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # Approach 2: Iterative approach
        stack = [[root, 1]]
        max_depth = 0
        while stack:
            stack_node, stack_depth = stack.pop()
            if stack_node:
                max_depth = max(max_depth, stack_depth)
                stack.append([stack_node.left, 1 + stack_depth])
                stack.append([stack_node.right, 1 + stack_depth])

        return max_depth

# 2.31 -> 10 min