# 2.18

class Solution:
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find number of car fleets crossing target line.

        Args:
            target (int): target distance
            position (list[int]): position of individual car
            speed (list[int]): speed of individual car

        Returns:
            int: number of car fleets crossing target line

        Time: O(n) - n = len(position)

        Space: O(n)
        """

        group = [[pos, sp] for pos, sp in zip(position, speed)]
        stack = []
        for pos, sp in sorted(group, reverse=True):
            time_needed = (target - pos) / sp

            if stack and time_needed <= stack[-1]:
                continue
            else:
                stack.append(time_needed)

        return len(stack)

s = Solution()
print(s.car_fleet(target = 10, position = [1,4], speed = [3,2]))
print(s.car_fleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))

# 2.28 -> 10 min