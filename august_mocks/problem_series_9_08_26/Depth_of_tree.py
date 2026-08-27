class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Find the depth of the given binary tree.

        Args:
            root: root node of given binary tree

        Returns:
            maximum depth of given binary tree(root-leaf length)

        Time: O(n) - n = total number of nodes
        Space: O(h)
        """

        stack = [[root, 1]]         # [[node, depth]]
        depth = 0

        while stack:
            stack_node, stack_depth = stack.pop()
            if stack_node:
                depth = max(depth, stack_depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth + 1])

        return depth






