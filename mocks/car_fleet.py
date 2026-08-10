# algorithm
# given two arrays and target destination, target = 10, position = [1,4], speed = [3,2]
# we will combine position and speed array together so we can access them jointly
# we will use sorted version of this array depending position -> [[4: 2], [1:3]]
# -> start processing from the ones that are closest to the destination
# for each car in array, calculate time_to_des (destination - position) / speed
# if stack is not empty then compare stack[-1] with current time_to_des
# if current time_to_des is smaller or equal to stack[-1] -> ignore it
# if current time_to_des is greater than stack[-1] then add to the stack
# in end return length of stack == number of fleets

class Solution:
    def car_fleets(self, target: int, position: list[int], speed: list[int]):
        """Find number of fleets that will arrive at destination.

        Args:
            target: int target destination for each car
            position: staring position of each car
            speed: speed of each car

        Returns:
            number of different car flets that will arrive at destination

        Time: O(n log n) - sorting
        Speed: O(n) - for res and stack
        """

        car = [[pos, sp] for pos, sp in zip(position, speed)]
        res = []
        for pos, sp in sorted(car, reverse = True):
            time_to_dest = (target - pos) / sp
            if res and time_to_dest <= res[-1]:
                continue

            res.append(time_to_dest)

        return len(res)

s = Solution()
#res = s.car_fleets(target = 10, position = [1,4], speed = [3,2])
res = s.car_fleets(target = 10, position = [4,1,0,7], speed = [2,2,1,1])
print(res)