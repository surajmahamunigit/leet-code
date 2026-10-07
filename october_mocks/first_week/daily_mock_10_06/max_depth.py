# 9.05

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Find the maximum depth of the binary tree.

        Args:
            root (TreeNode): root of the given binary tree

        Returns:
            int: maximum depth of the binary tree

        Time complexity: O(n) - n = total number of nodes in the tree

        Space complexity: O(h) - h = height of the given binary tree
        """

        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, height = stack.pop()

            if node:
                max_depth = max(max_depth, height)

                stack.append([node.left, 1 + height])
                stack.append([node.right, 1 + height])

        return max_depth
# 9.10 -> 5 minutes to solve the problem
# commit message suggestion -> feat: add maximum depth of binary tree solution (iterative)