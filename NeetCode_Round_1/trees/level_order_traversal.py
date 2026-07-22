from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelorderTraversal(self, root: TreeNode) -> list[list[int]]:
        """Find the level order traversal of given tree.

        Args:
            root: root node of given tree

        Returns:
            list of sub-list containing all node values at particular level from left to right

        Time: O(n) - n = length of tree
        Space: O(n)
        """

        result = []

        queue = deque()
        queue.append(root)          # add root to empty queue

        while queue:

            # step 1: add everything in queue for level to sublist
            sub_list = []

            for i in range(len(queue)):

                node = queue.popleft()          # remove from the queue

                if node:
                    sub_list.append(node.val)

                    queue.append(node.left)
                    queue.append(node.right)

            # step 2: make sure sub_list is not None
            if sub_list:
                result.append(sub_list)

        return result