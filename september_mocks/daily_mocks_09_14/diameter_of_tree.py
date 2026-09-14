# 1.50

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Find the diameter of the binary tree.

        Args:
            root (TreeNode): The root of the tree.

        Returns:
            int: The diameter of the tree.

        Time:
        Space:
        """
        diameter = 0

        def dfs(node):
            # base case
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        dfs(root)

        return diameter