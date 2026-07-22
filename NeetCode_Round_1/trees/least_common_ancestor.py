class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Find the least common ancestor for given nodes p and q.

        Args:
            root: root node of given tree
            p: first given node
            q: second given node

        Returns: lowest common ancestor node for the given node p and q

        Time: O(n) - n = length of tree
        Space: O(h) - h = height of the tree
        """

        curr = root

        while curr:

            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            else:
                return curr
