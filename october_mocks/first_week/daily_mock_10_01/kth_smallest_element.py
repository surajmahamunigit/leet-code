# 7.23

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        """Fid and return kth smallest element in given BST.

        Args:
            root (TreeNode): given Binary Search Tree
            k (int): kth smallest element (1-indexed position)

        Returns:
              int: value of the kth smallest element in the given BST

        Time complexity: O(h + k) - h = height of the given tree, k = 1-indexed position element

        Space complexity: O(h)
        """

        curr = root
        stack = []
        n = 0

        while curr or stack:

            # add each node on leftmost side to stack
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop one node at a time
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val

            curr = curr.right   # check right side subtree