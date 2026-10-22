# 3.54

from ds_helper import ListNode, build_list, list_to_values

class Solution:
    def reorderList(self, head: ListNode|None) -> None:
        """Reorder the given list.

        Args:
            head (ListNode|None): head node of the given list

        Returns:
            None: list is reordered in place

        Time complexity: O(n) - n = total number of nodes in the list

        Space complexity: O(1)
        """

        # find middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # join both in alternate manner
        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2



# 4.04 -> 10 minute sto solve problem without test cases
# git commit -> feat: add reorder the given list solution

s = Solution()
def check(values, expected):
    head = build_list(values)
    s.reorderList(head)
    assert list_to_values(head) == expected

check([1,2,3,4], [1,4,2,3])
check([1,2,3,4,5], [1,5,2,4,3])
check([1], [1])
check([1,2], [1,2])
print("all passed")