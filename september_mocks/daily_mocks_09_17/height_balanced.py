# 5.50

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """Find out if the given tree is height balanced or not.

        Args:
            root (TreeNode): root of the tree.

        Returns:
            bool: True if height is balanced, otherwise False.

        Time: O(n) - n = total number of nodes in the tree.

        Space: O(h) - h = height of the tree.
        """

        def dfs(node):

            # base case
            if not node:
                return [True, 0]            # [is_balanced, height]


            left = dfs(node.left)
            right = dfs(node.right)

            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [is_balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]