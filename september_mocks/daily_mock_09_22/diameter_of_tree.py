# 11.21
from platform import node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameter_of_tree(self, root: TreeNode) -> int:
        """Find the maximum diameter of tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            int: diameter of tree

        Time: O(n) - n = total number of nodes in given tree

        Space: O(h) - h = height of the binary tree
        """

        diameter = 0

        def dfs(node):

            #base condition
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, left+right)

            return 1 + max(left, right)

        dfs(root)

        return diameter

# 11.26 -> 5 min