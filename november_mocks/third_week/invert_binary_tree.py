# 2.31

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: TreeNode|None) -> TreeNode|None:
        """Invert the given binary tree.
        Args:
            root: head node of the given tree
        Returns:
            TreeNode|None: inverted binary tree
        Time complexity: O(n)  - n = total number of nodes in given tree
        Space complexity: O(h) - h = height of the tree
        """

        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root