class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        maxL, maxR = height[0], height[len(height) - 1]
        ans = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                if (min(maxL, maxR) - height[l]) > 0:
                    ans = ans + min(maxL, maxR) - height[l]
                maxL = max(maxL, height[l])
            else:
                r -= 1
                if (min(maxL, maxR) - height[r]) > 0:
                    ans = ans + min(maxL, maxR) - height[r]
                maxR = max(maxR, height[r])
        return ans
           
                
