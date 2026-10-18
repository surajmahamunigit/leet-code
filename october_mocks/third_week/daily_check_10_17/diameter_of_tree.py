# 4.32

# given -> binary tree
# asked -> diameter of the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.let = left
        self.right = right

class Solution:
    def diameter_of_tree(self, root: TreeNode|None) -> int:
        """Find the diameter of the tree.

        Args:
            root (ListNode|None): root of the given tree

        Returns:
             int: diameter of the given tree

        Time complexity: O(n) - n = total number of nodes in the tree

        Space complexity: O(h) - h = height of the tree
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

# 4.43 -> 11 minute sto solve the problem
# git commit -> feat: add diameter of binary tree solution