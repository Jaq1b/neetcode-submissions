class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #create a hashset to count the seen numbers
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        

        

       