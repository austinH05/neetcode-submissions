class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for x in range(len(nums)):
            if nums[x] > 0:
                break
            
            if x > 0 and nums[x] == nums[x - 1]:
                continue;

            l, r = x + 1, len(nums) - 1
            
            while l < r:
                ans = nums[x] + nums[l] + nums[r]
                
                if ans > 0:
                    r -= 1
                elif ans < 0:
                    l += 1
                else:
                    res.append([nums[x], nums[l], nums[r]])
                
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
