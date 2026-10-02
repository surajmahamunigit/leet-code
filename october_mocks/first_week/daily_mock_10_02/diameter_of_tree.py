# 2.31

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameter_of_tree_recursive(self, root: TreeNode) -> int:
        """Find the diameter of the given tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            int: diameter of the given tree

        Time complexity: O(n) - n = total number of nodes in given tree

        Space Complexity: O(h) - h = height of the given tree
        """

        diameter = 0

        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter