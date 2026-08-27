# 4.17

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find number of ar fleets crossing target line.

        Args:
            target: target distance
            position: position[i] represents position of car at index i from start line
            speed: speed[i] represents speed of car at i index

        Returns:
            number of car fleets crossing the target line

        Time: O(n) - n = len(position)
        Space: O(n)
        """

        stack= []
        group = [[pos, sp] for pos, sp in zip(position, speed)]

        for pos, sp in sorted(group, reverse=True):

            time_needed = (target - pos) / sp

            if stack and time_needed <= stack[-1]:
                continue
            else:
                stack.append(time_needed)
        return len(stack)

s = Solution()
assert s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
assert s.carFleet(10, [3], [3]) == 1
assert s.carFleet(100, [0,2,4], [4,2,1]) == 1
assert s.carFleet(10, [0,4,2], [2,1,3]) == 1
assert s.carFleet(10, [], []) == 0
assert s.carFleet(100, [69,61], [10,10]) == 2
print("pass")

# 4.24 -> 7 min to solve