class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Binary search

        left = 0
        right = len(nums) - 1

        # [3, 4, 5, 1, 2] -> mid=5 -> left side is sorted
        # [4, 5, 1, 2, 3] -> mid=1 -> right side sorted
        # roteded arrays always have left or right side sorted

        # number is given and search for it -> left < = right
        # if left side is sorted check target belongs in there, else
        # if right side is sorted, check target belongs there
        while left <= right:
            mid_index = (left + right) // 2
            mid_num = nums[mid_index]

            # target could be mid_num, on left side or right side
            # if mid_num == target
            if mid_num == target:
                return mid_index

                #  if left side of mid_num is sorted -> search like this
            if nums[left] <= mid_num:

                # left_num <= target < mid_num -> mid_num excluded
                if nums[left] <= target < mid_num:
                    right = mid_index - 1

                # target not in sorted side, search in unsorted side
                else:
                    left = mid_index + 1  # mid excluded


            # if right side is sorted -> search like this
            else:

                # same strategy
                if nums[mid_index] < target <= nums[right]:
                    left = mid_index + 1

                else:
                    right = mid_index - 1

        return -1  # not found


