# 2.20

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depth_of_tree(self, root: TreeNode) -> int:
        """Find the longest depth of the binary tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            int: longest depth of the binary tree

        Time complexity: O(n) - n = total number of nodes in given tree

        Space complexity: O(h) - h = height of the given tree
        """

        longest = 0

        if not root:
            return 0

        left = self.depth_of_tree(root.left)
        right = self.depth_of_tree(root.right)

        return max(left, right) + 1

