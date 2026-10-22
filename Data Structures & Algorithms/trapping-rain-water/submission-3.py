class Solution:
    # adjust l pointer till we height[l+1] < height
    # trapped_water += (height[l] - height[l+1])
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height)-1
        max_left = height[l]
        max_right = height[r]
        trapped_water = 0
        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, height[l])
                trapped_water += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                trapped_water += max_right - height[r]
            
        
        return trapped_water
