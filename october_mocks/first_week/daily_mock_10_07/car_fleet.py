# 11.52

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find number of car fleets crossing target.

        Args:
            target (int): target distance
            position (list[int]): integer array representing position of individual cars
            speed (list[int]): integer array representing speed of each car

        Returns:
             int: total number of car fleets crossing the target

        Time complexity: O(n log n) - n = len(position) -> sorting

        Space complexity: O(n)
        """

        group = [(pos, sp) for pos, sp in zip(position, speed)]
        stack = []
        for pos, sp in sorted(group, reverse=True):
            curr_time = (target - pos) / sp

            if stack and curr_time <= stack[-1]:
                continue

            stack.append(curr_time)

        return len(stack)

# 12 -> 8 minute sto solve problem
# git commit -> feat: add car fleet solution

s = Solution()
assert s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
assert s.carFleet(10, [3], [3]) == 1
assert s.carFleet(100, [0,2,4], [4,2,1]) == 1
assert s.carFleet(10, [0,4,2], [2,1,3]) == 1
assert s.carFleet(10, [], []) == 0
assert s.carFleet(100, [69,61], [10,10]) == 2