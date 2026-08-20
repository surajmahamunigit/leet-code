# 12.21
# given position, speed for each car and target distance, find out how many car fleets will cross target

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find how many car fleets will cross target line.

        Args:
            target: target distance
            position: position of each car from starting point
            speed: speed of each car

        Returns:
            number of car fleets crossing target line

        Time: O(n log n) - n = len(position)
        Space: O(n)
        """
        stack = []
        group = [(pos, sp) for pos, sp in zip(position, speed)]

        for pos, sp in sorted(group, reverse=True):
            curr_time_needed = (target - pos) / sp

            if stack and curr_time_needed <= stack[-1]:
                continue
            else:
                stack.append(curr_time_needed)

        return len(stack)

s = Solution()

assert s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
assert s.carFleet(10, [3], [3]) == 1
assert s.carFleet(100, [0,2,4], [4,2,1]) == 1
assert s.carFleet(10, [0,4,2], [2,1,3]) == 1
assert s.carFleet(10, [], []) == 0
assert s.carFleet(100, [69,61], [10,10]) == 2
print("passed")

# 12.29 -> 8 min to solve