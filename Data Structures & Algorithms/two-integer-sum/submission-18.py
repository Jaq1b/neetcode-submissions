class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        e = {}

        

        for i,n in enumerate(nums):
           
            
            
            diff = target - n
            if diff in e:
                return [e[diff],i]
            e[n] = i
        return []
            
