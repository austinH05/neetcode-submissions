class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxL = 0
        for i in range(len(height)):
            if i == 0:
                maxLeft[i]  = 0
            else:
                maxL = max(maxL, height[i - 1])
                maxLeft[i] = maxL
        maxR = 0
        for i in range(len(height) - 1, 0, -1):
            if i == len(height) - 1:
                maxRight[i] = 0
            else:
                maxR = max(maxR, height[i + 1])
                maxRight[i] = maxR
        water = [0] * len(height)
 
        for i in range(len(water)):
            ans = min(maxLeft[i], maxRight[i]) - height[i]

            if ans <= 0:
                water[i] == 0
            else:
                water[i] = ans
        return sum(water)

