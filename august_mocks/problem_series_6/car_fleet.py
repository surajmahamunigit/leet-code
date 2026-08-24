# 10.11
# given target, position, speed of each car. asked to find out number of cars passing target line.


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find number of car fleets crossing target line.

        Args:
            target: target distance
            position: position of each car from start line
            speed: speed of each car

        Returns:
            number of car fleets crossing target line

        Time: O(n log n) - n = len(speed)
        Space: O(n)
        """

        stack = []
        group = [[pos, sp] for pos, sp in zip(position, speed)]

        for pos, sp in sorted(group, reverse=True):
            time_needed = (target - position) / sp

            if time_needed <= stack[-1]:
                continue

            stack.append(time_needed)

        return len(stack)

# 10.17 -> 6 min to solve