# 7.15

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid(self, root: TreeNode) -> bool:
        """Find out if the given tree is valid or not.

        Args:
            root (TreeNode): given binary search tree

        Returns:
            bool: True if the given tree is BST, else False

        Time complexity: O(n) - n = total number of nodes in the tree

        Space complexity: O(h) - h = height of the given tree
        """

        def valid(node, left_val, right_val):

            if not node:
                return True

            if not (left_val < node.val < right_val):
                return False

            return valid(node.left, left_val, node.val) and valid(node.right, node.val, right_val)

        return valid(root, float('-inf'), float('inf'))