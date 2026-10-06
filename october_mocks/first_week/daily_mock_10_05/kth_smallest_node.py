# 8.20

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest_element(self, root: TreeNode, k: int) -> int:
        """Return teh value of kth smallest element in given tree.

        Args:
            root (TreeNode): root node of tree
            k (int): kth smallest element

        Returns:
              int: value of kth smallest element in given BST

        Time complexity: O(h + k) - h = height of the given BST, k: kth smallest element in given BST

        Space complexity: O(h)
        """
        curr = root
        stack = []
        n = 0
        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val

            curr = curr.right