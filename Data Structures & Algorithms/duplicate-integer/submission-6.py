class Solution: 
    def hasDuplicate(self, nums) -> bool:
        return len(nums) > len(set(nums))