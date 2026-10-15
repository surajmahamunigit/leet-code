# 2.42

# given -> a linked list
# asked -> to make a deep copy of given list

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: ListNode|None) -> ListNode|None:
        """Make a deep copy of the given linked list with next and random pointers.

        Args:
            head (ListNode|None): head node of the given linked list

        Returns:
            ListNode|None: head of the deep copied linked list

        Time complexity: O(n) - n = total number of nodes in given linked list

        Space complexity: O(n)
        """

        copy = {None:None}

        # walk the list to make new nodes
        curr = head
        while curr:
            new_node = ListNode(val=curr.val)
            copy[curr] = new_node
            curr = curr.next

        # walk list to copy pointers
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]



# 2.52 -> 10 minutes to solve the problem
# git commit -> feat: add copy list with random pointer solution

import random



def build(pairs):
    if not pairs:
        return None
    nodes = [ListNode(v) for v, _ in pairs]
    for i, (_, r) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if r is not None:
            nodes[i].random = nodes[r]
    return nodes[0]

def to_pairs(head):
    index, n, i = {}, head, 0
    while n:
        index[id(n)] = i
        n, i = n.next, i + 1
    out, n = [], head
    while n:
        out.append([n.val, index[id(n.random)] if n.random else None])
        n = n.next
    return out

def ids(head):
    out = set()
    while head:
        out.add(id(head))
        head = head.next
    return out

s = Solution()

def check(pairs):
    head = build(pairs)
    copy = s.copyRandomList(head)
    assert to_pairs(copy) == pairs        # same values and random wiring
    assert to_pairs(head) == pairs        # original left untouched
    assert not (ids(copy) & ids(head))    # deep copy: no shared nodes

assert s.copyRandomList(None) is None
check([[1, None]])
check([[1, 0]])
check([[3, None], [5, 2], [8, 0]])
check([[1, 1], [2, 1]])
check([[5, 2], [5, 0], [5, 1], [5, None]])
check([[0, 3], [1, None], [2, 0], [3, 2]])
check([[-7, None], [-7, None], [-7, None]])
check([[9, 0], [8, 1], [7, 2]])

random.seed(42)
big = [[random.randint(-10**4, 10**4), random.choice([None] + list(range(1000)))]
       for _ in range(1000)]
check(big)