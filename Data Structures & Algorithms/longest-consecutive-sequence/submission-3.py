class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        longest = 0

        for index, num in enumerate(nums):
            hm[num] = index

        for num in nums:
            if (num - 1) not in hm:
                length = 1
                while num + length in hm:
                    length += 1

                longest = max(length, longest)

        return longest
