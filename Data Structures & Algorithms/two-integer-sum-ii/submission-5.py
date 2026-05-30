class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i+=1
            elif numbers[i] + numbers[j] == target:
                return [1+i,1+j]
            else:
                j-=1

        
        return []


            
        