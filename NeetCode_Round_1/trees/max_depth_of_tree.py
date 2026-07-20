class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # step 1: also takes care of base-case
        stack = [[root, 1]]     # [node, depth]
        result = 0              # node might be null

        # step 2:
        while stack:

            node, depth = stack.pop()       # pop the top

            if node:                            # if node is not null
                result = max(result, depth)     # then compare its depth with result

                # append right and left
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result