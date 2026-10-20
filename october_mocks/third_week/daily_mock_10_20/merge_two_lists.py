from ds_helper import ListNode, build_list, list_to_values

# 1.44

class Solution:
    def mergeTwoLists(self, l1: ListNode|None, l2: ListNode|None) -> ListNode|None:
        """Merge the two given lists in sorted order.

        Args:
              l1, l2 (ListNode|None): head nodes of the given lists

        Returns:
            ListNode|None: head of the merged list

        Time complexity: O(n1 + n2) - n1, n2 = total number of node sin l1 and l2

        Space complexity: O(1)
        """

        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 <= val2:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        curr.next = l1 if l1 else l2

        return dummy.next

# 1.53 -> 9 minute sto solve problem, not including test writing time.
# git commit -> feat: add merge two sorted lists solution


if __name__ == "__main__":
    s = Solution()

    def check(values1, values2):
        result = s.mergeTwoLists(build_list(values1), build_list(values2))
        assert list_to_values(result) == sorted(values1+values2), f"failed for {values1}, {values2}"

    check([1,2,3],[4,5,6])
    check([2,3,4], [4,5,6])
    check([], [1,2,3])
    check([2,2], [2,2])
    check([-2,-1], [0,2])
    print("all passed")
