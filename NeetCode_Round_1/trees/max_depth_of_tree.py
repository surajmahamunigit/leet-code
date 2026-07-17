class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Returns the max depth of the tree.

        Args:
            root: root node of the given tree

        Returns:
            max depth of the tree

        Time: O(n) - visits every node once
        Space: O(h) - h = height of tree
        """

        # step 1: base case
        if not root:
            return 0

        # step 2:
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))