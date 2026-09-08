# 4.40

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Find the diameter of given binary tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            int: diameter of the given binary tree

        Time: O(n) - total number of nodes in tree
        Space: O(h) - h = height of binary tree
        """

        result = 0

        def dfs(curr):

            # base condition
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal result
            result = max(result, left+ right)

            return max(left, right) + 1


        dfs(root)
        return result

