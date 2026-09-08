# 6.34

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """Find out if the given tree is balanced or not.

        Args:
            root (TreeNode): given binary tree

        Returns:
            bool: True if tree is height-balanced, else False

        Time:
        Space:
        """
        def dfs(node):

            # base case
            if not node:
                return [True, 0]        # [is_balanced, height]

            left = dfs(node.left)
            right = dfs(node.right)

            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [is_balanced, max(left, right) + 1]


        return dfs(root)[0]