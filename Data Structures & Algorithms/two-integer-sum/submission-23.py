class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        e = {}
        for i,n in enumerate(nums):
            e[n] = i
        for i,n in enumerate(nums):
            
            diff = target - n
            if diff in e and e[diff]!=i:
                return [i,e[diff]]
        return []



        

        
        