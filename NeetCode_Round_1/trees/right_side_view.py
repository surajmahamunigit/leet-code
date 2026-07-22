from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """Find right side view of given tree.

        Args:
            root: root node of given tree

        Returns:
            list of values of right side nodes in the tree

        Time: O(n) - n = length of tree
        Space: O(n)
        """

        result = []     # to add all right side node values

        queue = deque([root])

        while queue:

            # step 1: pop queue nodes for each level
            right_node = None

            for i in range(len(queue)):

                node = queue.popleft()      # pop

                if node:                    # check
                    right_node = node       # temp

                    queue.append(node.left)     # append left to the queue
                    queue.append(node.right)    # append right to the queue

            # step 2: at end of for-loop -> right_node contains actual right node
            #       : check for None
            if right_node:
                result.append(right_node.val)

        return result



