class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def valid_bst(self, root: TreeNode) -> bool:
        """Find out if the given tree is valid BST or not.

        Args:
            root (TreeNode): The root of the given tree.

        Returns:
            bool: True if the given tree is valid BST, False otherwise.

        Time complexity: O(n) - n = total number of nodes in the tree.

        Space complexity: O(h) - h = height of the given tree
        """

        def valid(node, left_val, right_val):

            if not node:
                return True

            if not (left_val < node.val < right_val):
                return False

            return valid(node.left, left_val, node.val) and valid(node.right, node.val, right_val)

        valid(root, float('-inf'), float('inf'))