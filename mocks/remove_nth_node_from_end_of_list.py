# algorithm
# use dummy head and it starts before head node
# now we have to find nth - 1 node from list to remove nth node
# we will consider dummy as left node and head as right node
# until n -> right = right.next, n -= 1
# now we have made gap between left and right, treat it as constant window and move left and right one node at a time until right = Node
# that will leave left at previous node of target node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node(self, head: ListNode, n: int) -> ListNode:
        """Find and remove nth node from the end of the linked list.

        Args:
            head: head node of given list

        Returns:
            head node after removing nth node from the end of the list

        Time: O(m) - m = length of list
        Space: O(1)
        """

        dummy = ListNode(0, head)

        left = dummy
        right = head

        # move right n nodes ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # now move both left and right till right=None
        while right:
            left = left.next
            right = right.next

        # use left properly
        left.next = left.next.next

        return dummy.next
