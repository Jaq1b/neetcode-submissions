class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        e = {}
        for i in range(len(nums)):
            e[nums[i]] = 1 + e.get(nums[i],0)
        for i,n in e.items():
            if n>1:
                return i
                