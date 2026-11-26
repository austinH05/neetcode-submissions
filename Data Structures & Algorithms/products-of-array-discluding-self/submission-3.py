class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        res = [0] * len(nums)

        for x in range(len(nums)):
            if x == 0:
                pref[x] = 1
            else:
                pref[x] = nums[x - 1] * pref[x - 1]
        
        for x in range(len(nums) - 1, -1 , -1):
            if x == len(nums) - 1:
                suff[x] = 1
            else:
                suff[x] = nums[x + 1] * suff[x + 1]

        for x in range(len(nums)):
            res[x] = pref[x] * suff[x]

        return res