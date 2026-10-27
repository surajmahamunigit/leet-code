# 11.31

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_sorted_lists(self, l1: ListNode|None, l2: ListNode|None) -> ListNode|None:
        """Merger the two given sorted lists in sorted order.

        Args:
            l1 (ListNode|None): head node of the first sorted list
            l2 (ListNode|None): head node of the second sorted list

        Returns:
            ListNode|None: head node of the merged l1 and l2 in sorted order

        Time complexity: O(n1+n2) - n1, n2 = total number of nodes in l1 and l2

        Space complexity: O(1)
        """
        dummy = ListNode()
        tail = dummy
        while l1 and l2:

            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next

# 11.44 -> 13 minutes to write all the code
# git commit -> feat: add merge two sorted lists


s = Solution()

def build_list(values):
    dummy = ListNode()
    tail = dummy

    for val in values:
        tail.next = ListNode(val=val)
        tail = tail.next

    return dummy.next

def list_to_values(head, limit=100_000):
    out = []

    while head and len(out) <= limit:
        out.append(head.val)
        head = head.next

    return out

def check(values1, values2, expected):
    result = s.merger_sorted_lists(build_list(values1), build_list(values2))
    assert list_to_values(result) == expected

check([1],[], [1])
check([1], [2], [1,2])
check([], [], [])
check([1,2,3], [4,5,6],[1,2,3,4,5,6])
check([2,3,4],[4,5,6], [2,3,4,4,5,6])
check([1,3,5],[2,4,6],[1,2,3,4,5,6])
check([1,2,4], [1,3,5], [1,1,2,3,4,5])
check([], [1,2], [1,2])
print("all passed")