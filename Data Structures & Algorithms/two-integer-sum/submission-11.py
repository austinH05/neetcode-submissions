class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for index, num in enumerate(nums):
            hm[num] = index

        for x in range(len(nums)):
            diff = target - nums[x]

            if diff in hm and hm[diff] != x:
                return [x, hm[diff]]

        return []