class Solution:
    def top_k_freq(self, nums: list[int], k: int):
        """Find top k most frequent numbers in given array.

        Args:
            nums: list of integers
            k: top k frequent numbers

        Returns:
            list of top k numbers

        Time:
        Space:
        """

        # find the number count
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1


        # add to the frequency bucket
        bucket = [[] for _ in range(len(nums) + 1)]         # 0 index bucket
        for num, freq in count.items():
            bucket[freq].append(num)


        # read top-k
        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)

                if len(res) == k:
                    return res


s = Solution()
res = s.top_k_freq(nums = [1,2,2,3,3,3], k = 2)
print(res)