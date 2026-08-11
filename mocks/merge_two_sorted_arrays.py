# algorithm
# given heads of two sorted linked lists lets say list1, list2, n1 = list1.next, n2 = list2.next
# while list1 or list -> if list1 <= list2 -> list1.next = list2, list2.next = n1 then list1 becomes n1 and list2 becomes n2
# append remaining list1 or list2 -> if l1, list1.next = l1 -> else list2.next = l2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_sorted_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """Merge two sorted lists in sorted order and return a new head.

        Args:
            list1: head node of linked list 1
            list2: head node of linked list 2

        Returns:
            head node of linked list merged in sorted order

        Time: O(m+n) - m,n = length of linked list 1 and 2
        Space: O(1)
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2= list2.next
                tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next





        return dummy.next