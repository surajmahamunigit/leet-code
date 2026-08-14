# 7.05

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Returns how many car fleets will return to the destination.

        Args:
            target: target destination
            position: position[i] represents position of ith car from start position
            speed: speed[i] speeed of the ith car

        Returns:
           number of car fleets that will cross destination.

        Time: O(n log n) - n = len(position) - sorting
        Space: O(n)
        """

        stack = []
        group = [[pos, sp] for pos, sp in zip(position, speed)]

        for pos, sp in sorted(group, reverse = True):

            time_to_dest = (target - pos) / sp
            if stack and time_to_dest <= stack[-1]:
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
print("passed")

