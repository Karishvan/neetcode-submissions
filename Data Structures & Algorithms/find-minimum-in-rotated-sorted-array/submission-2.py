class Solution:
    def findMin(self, nums: List[int]) -> int:

      #Binary search
      left, right = 0, len(nums)-1

      while left <= right:
        #print(left)
        #print(right)
        mid = (left + right) // 2
        print(mid)
        if (mid+1 >= len(nums)):
            return nums[0]
        # elif (mid == 0):
        #     return nums[-1]
        elif (nums[mid] > nums[mid+1]):
            return nums[mid+1]
        elif (nums[mid] < nums[mid-1]):
            return nums[mid]
        elif (nums[mid] > nums[0]):
            left = mid + 1
        else:
            right = mid - 1
        
      return nums[mid]