# 11.58

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder_list(self, head: ListNode|None) -> ListNode|None:
        """Reorder the given list.

        Args:
            head (ListNode|None): head node of the given list

        Returns:
            ListNode|None: head node of the reordered list

        Time complexity: O(n) - n = total  number of nodes in given list

        Space complexity: O(1)
        """

        if not head:
            return None

        # split the list in half
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

        # join two halfs alternatively
        l1 = head
        l2 = prev
        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2

        return head

# 12.13 -> 15 minutes to solve the question and write test cases
# git commit -> feat: add reorder list solution

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

s = Solution()

def check(values, expected):
    result = s.reorder_list(build_list(values))
    assert list_to_values(result) == expected

check([1,2,3,4], [1,4,2,3])
check([], [])
check([1], [1])
check([1,2], [1,2])
check([1,2,3], [1,3,2])
print("all passed")