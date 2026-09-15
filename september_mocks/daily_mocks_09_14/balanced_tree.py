# 7.01

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balancedTree(self, root: TreeNode) -> bool:
        """Find out if the given tree is balanced or not.

        Args:
            root (TreeNode): root of the tree.

        Returns:
            bool: True if the given tree is balanced, False otherwise.

        Time: O(n) - n = total number of nodes in the tree.
        Space: O(h) - h = height of the tree
        """

        def dfs(node):
            # base case
            if node is None:
                return [True, 0]


            left = dfs(node.left)
            right = dfs(node.right)

            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [is_balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]