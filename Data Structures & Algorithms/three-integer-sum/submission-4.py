from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        startingNums = collections.defaultdict(list)
        #print(numsSorted)
        res = []
        for i in range(len(numsSorted)):
            num = numsSorted[i]
            #Run two sum
            l,r = i+1,len(numsSorted)-1
            target = -1 * numsSorted[i]
            while (l < r):
                
                # print(target)
                # print(numsSorted[l])
                # print(numsSorted[r])
                # print("----------")
                # l+=1
                # r-=1
                if (numsSorted[l] + numsSorted[r] < target):
                    l+=1
                elif (numsSorted[l] + numsSorted[r] > target):
                    r-=1
                else:
                    #print("target")
                    print(startingNums)
                    if (numsSorted[i] not in startingNums or numsSorted[l] not in startingNums[numsSorted[i]]):
                        #print("HIT ", numsSorted[i], " with dict ", startingNums)
                        startingNums[numsSorted[i]].append(numsSorted[l])
                        res.append([numsSorted[i], numsSorted[l], numsSorted[r]])
                    l+=1
                    
        return res
                            
                    
