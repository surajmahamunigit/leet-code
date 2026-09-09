# 9.15

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Find the diameter of the given binary tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            int: diameter of the given binary tree

        Time: O(n) - n = number of nodes in binary tree
        Space: O(h) - h = height of the binary tree
        """
        diameter = 0

        def dfs(curr):

            # base case
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal diameter
            diameter = max(diameter, left+right)

            return 1 + max(left, right)

        dfs(root)

        return diameter

# 9.21 -> 6 min