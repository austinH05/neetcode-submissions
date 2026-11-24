class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0]* len(nums)
        suff = [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pref[i] = 1
            else:
                pref[i] = nums[i - 1] * pref[i - 1]
            
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suff[i] = 1
            else:
                suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(len(res)):
            res[i] = pref[i] * suff[i]

        return res