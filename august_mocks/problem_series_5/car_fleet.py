# 1.14
# given two arrays position and speed and asked to return number of distinct fleets
# sorte the cars according to their position in descending order -> calculate time need for each car
# if stack is empty add the time needed to the stack
# if its not empty -> compare last entry in stack with current time needed
# if last entry is equal or larger than curr needed time -> ignore, it will join the fleet
# if its more -> add to stack
# reurn length of stack

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Find number of car fleets crossing the target.

        Args:
            target: target distance
            position: position of each car from start line
            speed: speed of each car

        Returns:
            numbers of distinct car fleets crossing the target

        Time: O(n) - n = len(position)
        Space: O(n)
        """

        stack = []

        group = [[pos, sp] for pos, sp in zip(position, speed)]

        for pos, sp in sorted(group, reverse=True):
            time_needed = (target - pos) / sp

            if stack and stack[-1] >= time_needed:
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
print("passed")

# 1.29 -> 15 min to solve