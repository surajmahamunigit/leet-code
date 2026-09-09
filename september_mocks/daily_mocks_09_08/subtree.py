# 11.27

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Find out if given trees are same or not.

        Args:
            p, q (TreeNode): given binary trees

        Returns:
            bool: True if given trees are same else False

        Time: O(n) - n = total number of nodes in p
        Space: O(h) - h = height of p
        """

        # if both are empty
        if not p and not q:
            return True

        # if only one is empty
        if not p or not q:
            return False

        # if values are different
        if p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def isSubtree(self, root: TreeNode, subroot: TreeNode) -> bool:
        """Find out if the given tree is subtree of another tree.

        Args:
            root, subroot (TreeNode): given trees

        Returns:
            bool: True if subroot is subtree of root else False

        Time: O(m*n) - m = number of nodes in subroot tree, n = number of nodes in root tree
        Space: O(h) - h = height root tree
        """

        # root is empty
        if not root:
            return not subroot      # if root is empty, there is chance subroot might be empty too

        # check both trees are same or not for current node of root tree
        if self.sameTree(root, subroot):
            return True

        # if its not true for current node, lets try with left side and right side nodes of current node
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

# 11.41 -> 14 min to solve
# no help taken