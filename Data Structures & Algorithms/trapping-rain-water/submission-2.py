class Solution:
    # adjust l pointer till we height[l+1] < height
    # trapped_water += (height[l] - height[l+1])
    def trap(self, height: List[int]) -> int:
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        max_left = 0
        for i in range(1, len(height)):
            max_left = max(max_left, height[i-1])
            prefix_max[i] = max_left
        max_right = 0
        for j in range(len(height)-2, -1, -1):
            
            max_right = max(max_right, height[j+1])
            suffix_max[j] = max_right
      
        trapped_water = 0
        for i in range(len(height)):
            tr = (min(prefix_max[i], suffix_max[i]) - height[i])
            if tr > 0:
                trapped_water += tr
        
        return trapped_water
