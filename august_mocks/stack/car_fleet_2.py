# 2.38

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find out how many car fleets will cross target destination.

        Args:
            target: target destination
            position: position of each car from the starting point
            speed: speed of each car

        Returns:
            number of car fleets crossing target

        Time: O(n log n) - n = len(position) - sorting
        Space: O(n))
        """

        group = [[pos, sp] for pos, sp in zip(position, speed)]
        stack = []

        for pos, sp in sorted(group, reverse=True):
            time_to_target = (target - pos) / sp

            if stack and stack[-1] >= time_to_target:
                continue
            else:
                stack.append(time_to_target)

        return len(stack)

s = Solution()
assert s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
assert s.carFleet(10, [3], [3]) == 1
assert s.carFleet(100, [0,2,4], [4,2,1]) == 1
assert s.carFleet(10, [0,4,2], [2,1,3]) == 1
assert s.carFleet(10, [], []) == 0
assert s.carFleet(100, [69,61], [10,10]) == 2   # the floor-division trap from before
print("passed")

# 2.46 -> 8 min to solve