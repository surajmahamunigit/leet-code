# 12.28

class Solution:
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find number of car fleets crossing target line.

        Args:
            target: target distance from starting mile 0
            position: list representing position of each car from staring mile 0
            speed: list representing speed of each car

        Returns:
            int: number of car fleets crossing target line

        Time complexity: O(n) - n = len(position)

        Space complexity: O(1)
        """

        # target 9, position = [1,2,3,4], speed = [1,2,3,4]

        stack = []

        for pos, sp in zip(position, speed):
            time_needed = (target - pos) / sp

            if stack and time_needed <= stack[-1]:
                continue
            else:
                stack.append(time_needed)
        return len(stack)

s = Solution()

def check(target, position, speed, expected):
    result = s.car_fleet(target, position, speed)
    assert result == expected

check(4,[1], [1], 1)
check(5, [0], [2], 1)
check(10, [1,2,3,4], [1,2,3,4], 1)
check(10, [4,3,2,1], [4,3,2,1], 4)
check(10, [2,3,1,4], [3,2,4,1], 3)
print("all tests passed")