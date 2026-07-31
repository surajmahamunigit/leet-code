class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """Find kth smallest node in the given BST.

        Args:
            root: root node of given BST

        Returns:
            kth smallest node in given BST

        Time: O(n) - n = number of nodes
        Space: O(h) - h = height of BST
        """

        n = 0        # to keep count of processed nodes
        stack = []    # to add left side nodes
        curr = root

        while curr or stack:

            while curr:
                stack.append(curr)      # add curr to stack
                curr = curr.left        # move left to add it

            # Note: no left remained to add -> no left to process -> process curr == process parent
            # process time
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val

            # move to right node to precess it
            curr = curr.right
