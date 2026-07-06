class Solution:
    def carFleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        """
        Args:
            target: target distance
            positions: list representing the position of each car
            speeds: list representing the speed of each car

        Returns:
            number of car fleets

        Time: O(n log n) - n = len(positions)
        Space: O(n)
        """

        pair = [[position, speed] for position, speed in zip(positions, speeds)]    # [position : speed] pair for each car

        stack = []      # stack to store time taken by each car to each target

        for position, speed in sorted(pair, reverse=True):

            # Add the time taken by car to each target
            time_to_target = (target - position) / speed
            stack.append((time_to_target))

            # if there are more than two car times in stack
            # Compare them, if car at top of stack (stack[-1]) needs less time to get to target than stack[-2], it will follow it till target because stack[-2] car is slow
            # so counts as one fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

result = Solution().carFleet(target = 10, positions = [4,1,0,7], speeds = [2,2,1,1])
print(result)
