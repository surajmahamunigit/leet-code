# 7.19

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Find the lowest common ancestor of node p and q.

        Args:
            root (TreeNode): given binary Search Tree
            p, q (TreeNode): nodes from  the given tree

        Returns:
            TreeNode: lowest common ancestor of p and q

        Time complexity: O(h) - h = height of in given BST

        Space complexity: O(1)
        """

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else:
                return curr