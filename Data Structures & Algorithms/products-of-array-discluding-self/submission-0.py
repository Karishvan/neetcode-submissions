class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        res = []
        product = 1

        for num in nums:
            product = num * product
            pre.append(product)
            
        product = 1
        for i in range (len(nums)-1, -1, -1):
            num = nums[i]
            product = num * product
            post.append(product)
        # pre.pop()
        # post.pop()
        # print(pre)
        # print(post)
        for i in range (len(nums)):
            # print(pre[i])
            # print(post[len(nums)-1-i])
            res.append(pre[i] * post[len(nums)-1-i])
        
        return res
        
        