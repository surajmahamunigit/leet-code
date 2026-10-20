# 12.49

# given -> linked list
# asked -> to reverse it

from ds_helper import ListNode, build_list, list_to_values

class Solution:
    def reverseList(self, head: ListNode|None) -> ListNode|None:
        """Reverse the given linked list.

        Args:
            head (ListNode|None): head node of the given linked list

        Returns:
            ListNode|None: head node of the reversed linked list

        Time complexity: O(n) - n = total number of nodes in the linked list

        Space complexity: O(1)
        """

        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# 12.58 -> 9 minutes to solve the problem
# git commit -> feat: add reverse linked list solution


s = Solution()

def check(values):
    result = s.reverseList(build_list(values))
    assert list_to_values(result) == values[::-1], f"failed for {values}"

check([1,2,3,4])
check([])
print("all passed")