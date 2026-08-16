# 8.48

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find how many car fleets will cross destination line.

        Args:
            target: destination for cars
            position: position[i] represents position of ith  car
            speed: speed[i] represents speed of ith car

        Returns:
            total number of car fleets crossing destination

        Time: O(n log n) - n = len(position)
        Space: O(n)
        """
        stack = []
        group = [[pos, sp] for pos, sp in zip(position, speed)]

        for pos, sp in sorted(group, reverse=True):
            time_to_dest = (target - pos) / sp
            if stack and stack[-1] >= time_to_dest:
                continue
            else:
                stack.append(time_to_dest)

        return len(stack)

s = Solution()
assert s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
assert s.carFleet(10, [3], [3]) == 1
assert s.carFleet(100, [0,2,4], [4,2,1]) == 1
assert s.carFleet(10, [0,4,2], [2,1,3]) == 1
assert s.carFleet(10, [], []) == 0
assert s.carFleet(100, [69,61], [10,10]) == 2   # floor-division trap
print("passed")

# 9.01 -> 13 min to finish