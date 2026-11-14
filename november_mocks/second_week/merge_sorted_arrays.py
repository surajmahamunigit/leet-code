# 10.15

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_sorted_lists(self, l1: ListNode|None, l2: ListNode|None) -> ListNode:
        """Merge the given two sorted lists in sorted order.

        Args:
            l1|None: first sorted list
            l2|None: second sorted list
        Returns:
            ListNode|None: merged list in sorted order
        Time complexity: O(L1 + L2) - L1, L2 = total number of nodes in the given lists l1 and l2
        Space complexity: O(1)
        """
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 <= val2:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next

def build_list(values):
    dummy = ListNode()
    tail = dummy

    for val in values:
        tail.next = ListNode(val=val)
        tail = tail.next

    return dummy.next

def list_to_values(head, limit=100_000):
    result = []
    curr = head

    while curr:
        result.append(curr.val)
        curr = curr.next

    return result

s = Solution()

def check(values1, values2, expected):
    result = s.merge_sorted_lists(build_list(values1), build_list(values2))
    assert list_to_values(result) == expected

check([], [], [])
check([],[1], [1])
check([1], [1], [1,1])
check([1], [2], [1,2])
check([1,3], [2], [1,2,3])
check([4,5], [1], [1,4,5])
print("all tests passed")
