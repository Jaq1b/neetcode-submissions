class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        e = set()

        for num in nums:
            if num in e:
                return True
            e.add(num)
        return False
        