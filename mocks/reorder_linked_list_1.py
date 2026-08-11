# algorithm
# given aven list and asked to reorder it
# [1,2,3,4] -> [1, 4, 2, 3]
# we know the head, slow = head, fast = head.next for balanced split
# while fast and fast.next -> slow = slow.next, fast = fast.next.next
# when loop ends, slow will land exactly  on node where 1st half of list should finish.
# head -> slow is one part of list, slow.next -> None represents second half.
# now reverse the second half
# then attach one node from 1st list and 2nd from second list and continue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder_linkedlist(self, head: ListNode) -> ListNode:
        """Reorder the given list and return head of new linked list.

        Args:
            head: head node of given list

        Returns:
            head node of new reordered linked list

        Time: O(n) - n = length of linked list
        Space: O(1)
        """

        slow = head
        fast = head.next        # use it lie this two split list into two equal halfs

        # split into two half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next                   # when loop ends, slow will represent last node of 1st half.


        # reverse second half
        curr = slow.next                            # start node of second half
        slow.next = None                            # splitting done
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node                         # in end prev is head of second reversed half.

        # now join both lists
        l1 = head
        l2 = prev
        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2  = temp2

