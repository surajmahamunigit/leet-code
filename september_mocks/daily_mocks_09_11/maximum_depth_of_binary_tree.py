# 7.20

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthRecursive(self, root: TreeNode) -> int:
        """Find the maximum depth of a binary tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
             int: maximum depth of the tree

        Time: O(n) - n = total number of nodes in the tree
        Space: O(h) - h = height of the given tree
        """

        # base case
        if not root:
            return 0

        left = self.maxDepthRecursive(root.left)
        right = self.maxDepthRecursive(root.right)

        return 1 + max(left, right)

    def maxDepthIterative(self, root: TreeNode) -> int:
        """Find the maximum depth of a binary tree.

        Args:
            root (TreeNode): given binary tree

        Returns:
            int: maximum depth of the tree

        Time: O(n) - n = total number of nodes in the tree
        Space: O(h) - h = height of the given tree
        """

        stack = [[root, 1]]     # first mistake, not counting the root as height 1
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)           # second mistake, if only node exist, then compare height with max_depth

                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])       # mistake three, stupid mistake typing root instead of node

        return max_depth

# 7.30 -> 10 min
# and we will use iterative approach because pyhon can make around 1000 recursive calls and  if the tree is skewed and tree has height bigger than 1000, it will fail. correct me if i am wrong.