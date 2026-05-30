class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set()
        isFalse = set()
        prev = {}

        jumps, i = nums[0], 0
        count = 0

        while i < len(nums)-1:
            # count += 1
            # if count > 10:
            #     return False
            # print(i, jumps)
            if jumps < 0:
                return False
            if nums[i] == 0 or i in isFalse:
                isFalse.add(i)
                #print("NUMS IS 0", prev)
                if not prev:
                    return False
                print(i, prev)
                tmp = prev[i]
                del prev[i]
                i = tmp
                
                nums[i] -= 1
                print("JUMPS", jumps)
                continue
            
            jumps = nums[i]
            if i+jumps not in visited:
                prev[i+jumps] = i
            else:
                nums[i]-=1
                continue
            visited.add(i)
            
            
            print(prev)
            i += jumps
            
        
        return True
        
        
        