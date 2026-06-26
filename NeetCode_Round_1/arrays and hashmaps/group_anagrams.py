class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {}
        frequency = [[] for occurrence in range(len(nums) + 1)]

        # Count the occurrence
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Add num and occurrence to the bucket list
        for num, occurrence in count.items():
            frequency[occurrence].append(num)

        # Read top k num
        result = []

        for index in range(len(frequency) - 1, 0, -1):
            for num in frequency[index]:
                result.append(num)

                if len(result) == k:
                    return result

result = Solution().topKFrequent(nums=[1,1,2,3,4,5,5], k=2)
print(result)