# 6.12

# given binary tree
# asked to find peth of it

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """Find the maximum depth of the binary tree.

        Args:
            root (TreeNode): root of the given binary tree

        Returns:
             int: maximum depth of the binary tree

        Time complexity: O(n) - n = total number of nodes in the tree

        Space complexity: O(h) - h = height of the given tree
        """

        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, height = stack.pop()

            if node:
                max_depth = max(max_depth, height)

                if node.left:
                    stack.append([node.left, height + 1])
                if node.right:
                    stack.append([node.right, height + 1])

        return max_depth

# 6.18 -> 6 minutes to solve problem
# git commit -> feat: add maximum depth of binary tree solution

