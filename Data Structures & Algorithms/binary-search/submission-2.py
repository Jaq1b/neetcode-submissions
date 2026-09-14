class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)

        while l<r:
            if nums[l]==target:
                return l
            else:
                l+=1
        
        return -1
        
        

        