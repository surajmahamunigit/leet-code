# 2.43
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root: TreeNode|None) -> int:
        """Find the maximum depth of the given binary tree.
        Args:
            root: head node of the given binary tree
        Returns:
            int: maximum depth of the given binary tree

        Time complexity: O(n) - n = total number of nodes in given tree

        Space complexity: O(h) - h = height of the given tree
        """

        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return 1 + max(left, right)