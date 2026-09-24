class Solution:
    def twoSum(self, nums, target) -> List:
        solution = {}
        for x in range(len(nums)):
            solution[nums[x]] = x
        
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in solution and x != solution[diff]:
                return [x, solution[diff]]
        return []