from ds_helper import ListNode, build_list, list_to_values

# 3.07

class Solution:
    def removeNthNode(self, head: ListNode|None, n: int) -> ListNode|None:
        """Remove the Nth node from the end of the list.

        Args:
            head (ListNode|None): head node of the given linked list
            n (int): position of node to remove, counted from the end

        Returns:
            ListNode|None: head node after removing nth node from end of the list

        Time complexity: O(l) - l = total number of nodes in given list

        Space complexity: O(1)
        """

        dummy = ListNode(next=head)
        slow = dummy
        fast = head

        # move fast n nodes ahead of head
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        # move fast and slow till fast = None
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

# 3.15 -> 8 minutes to solve problem not including tests writing time
# git commit -> feat: add remove nth node from end solution


s = Solution()

def check(values, n):
    expected = values[:]
    del expected[len(values) - n]

    result = s.removeNthNode(build_list(values), n)
    assert list_to_values(result) == expected, f"failed for {values}, n = {n}"

check([1,2,3,4,4], 3)
check([1,2,3,4], 1)
check([1,2,3,4], 4)
check([5, 1, 5], 1)
check([5, 1, 5], 3)
check([1], 1)
check(list(range(30)), 15)

print("all passed")