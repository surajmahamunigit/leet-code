# 10.34

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Find the lowest common ancestor for given two nodes.

        Args:
            root (TreeNode): given BST
            p, q (TreeNode): nodes in BST

        Returns:
            TreeNode: lowest common ancestor of given nodes

        Time complexity: O(h) - h = height of the given tree (no recursion)

        Space complexity: O(1)
        """

        curr = root
        while curr:

            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr