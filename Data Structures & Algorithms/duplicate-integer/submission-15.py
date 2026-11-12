class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        e = set()
        for i in range(len(nums)):
            e.add(nums[i])
        
        if len(nums) == len(e):
            return False
        else:
            return True