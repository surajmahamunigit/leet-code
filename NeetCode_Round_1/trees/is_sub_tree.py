class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """ Find out if t is subtree of s.

        Args:
            s: first tree node
            t: second tree node

        Returns:
            True if t is subtree of s, otherwise False

        Time: O(m.n) - m, n = length of first and second tree
        Space: O(h1 + h2) - h1, h2 = heights of first and second tree
        """

        # step 1: if t = None -> subtree
        if not t:
            return True

        # step 2: if s = None -> not subtree
        if not s:
            return False

        # step 3: if both have values -> compare them in sameTree()
        if self.sameTree(s, t):
            return True

        # step 4: values didnt match -> compare t with s.left and s.right subtrees
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def sameTree(self, s: TreeNode, t: TreeNode):

        # step 3.1: if both values are None -> subtree
        if not s and not t:
            return True

        # step 3.2: both values are equal -> compare s and t for their left and right nodes
        if s and t and (s.val == t.val):
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        # otherwise
        return False