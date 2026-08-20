# 11.04
# given head node of the original list with next and random pointer, asked to make deep copy of it and return its head
# walk the original list and create new nodes with current node value
# walk original list again and copy next and random pointer

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        """Make deep copy of given linked list and return its head node.

        Args:
            head: head node of given linked list

        Returns:
            make deep copy of given list and return its head node

        Time: O(n) - n = length of given linked list
        Space: O(n)
        """

        copy_list = {None:None}

        # walk original list to create new nodes
        curr = head

        while curr:
            new_node = Node(curr.val)
            copy_list[curr] = new_node
            curr = curr.next

        # walk original list again to copy pointers
        curr = head

        while curr:
            copy_list[curr].next = copy_list[curr.next]
            copy_list[curr].random = copy_list[curr.random]
            curr = curr.next

        return copy_list[head]


def build_list(pairs):
    if not pairs:
        return None
    nodes = [Node(v) for v, _ in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for node, (_, r) in zip(nodes, pairs):
        node.random = nodes[r] if r is not None else None
    return nodes[0]

def to_pairs(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    index = {id(n): i for i, n in enumerate(nodes)}
    return [(n.val, index[id(n.random)] if n.random else None) for n in nodes]

def is_deep_copy(orig_head, copy_head):
    o, c = orig_head, copy_head
    while o:
        if o is c:
            return False
        o, c = o.next, c.next
    return True

s = Solution()
p1 = [[7,None],[13,0],[11,4],[10,2],[1,0]]
orig1 = build_list(p1)
copy1 = s.copyRandomList(orig1)
assert to_pairs(copy1) == [(v, r) for v, r in p1]
assert is_deep_copy(orig1, copy1)

assert s.copyRandomList(None) == None

p2 = [[1,None]]
orig2 = build_list(p2)
copy2 = s.copyRandomList(orig2)
assert to_pairs(copy2) == [(1, None)]
assert is_deep_copy(orig2, copy2)

print("passed")

# 11.14 -> 10 min to solve