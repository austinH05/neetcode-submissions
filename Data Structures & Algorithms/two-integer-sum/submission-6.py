class Solution:
    def twoSum(self, nums, target) -> List:
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in hashmap and x != hashmap[diff]:
                return [x, hashmap[diff]]