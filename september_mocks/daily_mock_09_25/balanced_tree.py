# 7.58

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height_balanced(self, root: TreeNode) -> int:
        """Find out if the given tree is height balanced or not.

        Args:
            root (TeeNode): given binary tree

        Returns:
            bool: True if the given tree is height balanced else False

        Time: O(n) - n = total number of nodes in given tree

        Space: O(h) - h = height of the given tree
        """

        def dfs(node):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [is_balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

