class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while (l <= r):
            mid = (l+r)//2
            #print(mid)
            if (nums[mid] == target):
                return mid
            #Are we in left sorted portion
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            #Are we in right sorted portion
            else:
                #print("else")
                if nums[mid] < target <= nums[-1]:
                    l = mid+1
                else:
                    r = mid-1
        
        return -1