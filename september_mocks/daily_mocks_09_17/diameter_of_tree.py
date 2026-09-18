# 5.03

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Find the diameter of the given binary tree.

        Args:
            root (TreeNode): root node of binary tree.

        Returns:
            int: diameter of the given binary tree.

        Time: O(n) - n = total number of nodes in the tree.

        Space: O(h) - h = height of the balanced tree
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