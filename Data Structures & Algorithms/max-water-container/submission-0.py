class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ans = 0

        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            product = width * height
            ans = max(product, ans)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

        return ans 