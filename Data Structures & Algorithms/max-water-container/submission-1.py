class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        max_area = 0
        while (i < j):
            width = j-i
            height = min(heights[i], heights[j])
            area = width * height
            #print(i)
            #print(j)
            max_area = max(max_area, area)
            if (heights[i] < heights[j]):
                i+=1
            else:
                j-=1

        return max_area
        