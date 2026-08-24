class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        e = set()

        for s in nums:
            if s in e:
                return True
            
            e.add(s)
        
        return False
        