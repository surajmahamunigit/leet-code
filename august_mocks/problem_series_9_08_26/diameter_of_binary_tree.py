# 9.16

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Find the diameter of given binary tree.

        Args:
            root: root node of given tree

        Returns:
            diameter of given binary tree

        Time: O(n) - n = total number of nodes
        Space: O(h) - h = height of tree
        """

        result = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal result
            result = max(result, left + right)
            return 1 + max(left, right)

        dfs(root)

        return result