class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height)-1
        while l < r:
            lower = min(height[l], height[r])
            water_level = lower * (r - l)
            
            if water_level > max_water:
                max_water = max(max_water, water_level)
                
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            elif height[l+1] > height[r-1]:
                r -= 1
            else:
                l += 1
        return max_water
                
            
        