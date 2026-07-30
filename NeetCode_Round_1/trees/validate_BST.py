class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """Find out if the given binary search tree is valid or not.

        Args:
            root: root node of given BST

        Returns:
            True if given BST is valid, otherwise False

        Time: O(n) - n = number of nodes
        Space: O(h) - h = height of BST
        """

        def valid(node, left, right):

            # rule 1 : base case
            if not node:
                return True             # valid BST

            # rule 2: node.val must be between left and right values
            if not (left < node.val and node.val < right):
                return False

            # if its in between range -> call valid() on left and right node with new left and right limits
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))


        return valid(root, float("-inf"), float("inf"))