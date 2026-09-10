class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        e = set()
        for i in nums:
            if i in e:
                return True
            e.add(i)
        
        return False