class Solution:
    def twoSum(self, nums, target) -> List:
        hm = {}

        for index, num in enumerate(nums):
            hm[num] = index

        res = []
        for x in range(len(nums)):
            diff = target - nums[x];
            if diff in hm and x != hm[diff]:
                res.extend([x, hm[diff]])
                return res

       