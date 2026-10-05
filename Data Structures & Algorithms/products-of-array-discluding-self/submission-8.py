class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1] * len(nums)
        post = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = post
            post*=nums[i]


                
            
        pre=1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
        
        return ans
            

            



        