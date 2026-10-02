# 3.01

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kth_smallest_element(self, root: TreeNode, k: int) -> int:
        """Return value of kth smallest element in the BST tree.

        Args:
            root (TreeNode): given BST
            k (int): kth smallest element

        Returns:
            int: value of the kth smallest element in tree

        Time complexity: O(h + k) - h = height of the tree, k = kth smallest value in tree
        (h because we travel all the way to the left most node, k pops to find smallest value)

        Space complexity: O(h)
        """

        stack = []
        n = 0
        curr = root

        while curr or stack:

            # add all the left side node sto stack
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop the last one
            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val

            # if not same, then look on to the right side of curr, we might find it there
            curr = curr.right