# 7.26

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validate_bst(self, root: TreeNode) -> bool:
        """Validate the given BST.

        Args:
            root (TreeNode): The root of the BST.

        Returns:
            bool: True if the given BST is valid, False otherwise.

        Time complexity: O(n) - n = number of nodes in the BST.

        Space complexity: O(h) - h = height of the given BST
        """

        def valid(node, left_val, right_val):

            if not node:
                return True

            if not left_val < node.val < right_val:
                return False

            return valid(node.left, left_val, node.val) and valid(node.right, node.val, right_val)

        return valid(root, float('-inf'), float('inf'))