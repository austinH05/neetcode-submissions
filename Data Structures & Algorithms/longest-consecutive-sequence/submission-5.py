class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}

        for index, num in enumerate(nums):
            hm[num] = index

        sol = 0
        
        for x in range(len(nums)):
            length = 1
            if (nums[x] - 1) not in hm:
                while (nums[x] + length) in hm:
                    length += 1
                
                sol = max(length, sol)

        return sol