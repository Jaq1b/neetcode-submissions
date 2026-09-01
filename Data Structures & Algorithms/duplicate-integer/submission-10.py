class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        e = set()
        for i in nums:
            if i not in e:
                e.add(i)
            else:
                return True
        
        return False
        