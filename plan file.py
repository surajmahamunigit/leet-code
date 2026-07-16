step 1:
slow = head = 1
fast = head = 1

step 2: (fast = 1, fast.next = 2)
slow = slow.next = 2
fast = fast.next.next = 3

step 3: (fast=3, fast.next = 4)
slow = slow.next = 3
fast = fast.next.next = 5

step 4: (fast= 5, fast.next = 6)
slow = slow.next = 4
fast = fast.next.next = None

result = middle = slow = 4
