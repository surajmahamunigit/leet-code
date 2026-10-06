# 12.12

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanced_tree(self, root: TreeNode) -> bool:
        """Find out if the given tree is height balanced or not.

        Args:
            root (TreeNode): root of the given tree

        Returns:
            bool: true if the given tree is height balanced else False

        Time complexity: O(n) - n = total number of nodes in given tree

        Space complexity: O(h) - h = height of the given tree
        """

        def dfs(node):

            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [is_balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]