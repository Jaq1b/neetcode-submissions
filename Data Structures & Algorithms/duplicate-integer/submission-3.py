class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #create a hashset to count the seen numbers
        for num in nums: #search through nums using num
            if num in seen: #if num is in seen(hashset)
                return True #return True break loop
            seen.add(num) #if not true add num to seen hashset
        return False #endcase if none i caught
        

        

       