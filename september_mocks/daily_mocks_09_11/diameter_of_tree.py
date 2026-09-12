# 7.50

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Find the diameter of the given tree.

        Args:
              root (treeNode): given binary tree

        Returns:
              int: diameter of the given tree

        Time: O(n)- n = total number of nodes in the tree
        Space: O(h) - h = height of the given tree
        """

        diameter = 0

        def dfs(node):

            # base case
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, left + right)      # diameter till the node

            return 1 + max(left, right)         # height till the node

        dfs(root)

        return diameter

# 8.01 -> 11 min