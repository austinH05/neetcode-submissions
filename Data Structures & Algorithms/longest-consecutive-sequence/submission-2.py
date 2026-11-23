class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        sol = 0

        for x in range(len(nums)):
            if (nums[x] - 1) not in numSet:
                count = 1
                num = nums[x]
                while num + 1 in numSet:
                    count += 1
                    num += 1
                sol = max(sol, count)

        return sol
                
