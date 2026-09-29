class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for ind in range(len(nums)):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            
            l, r = (ind + 1), len(nums) - 1
            while l < r:
                target = nums[ind] + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([nums[ind], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
                    
            
