class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        e = set()
        for i in nums:
            
            e.add(i)
        
        if len(e) != len(nums):
            return True
        else:
            return False
        
            


        