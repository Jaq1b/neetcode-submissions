class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        e = {}

        for i,n in enumerate(numbers):
            diff = target - n
            if diff in e:
                return [e[diff]+1,i+1]
            
            e[n] = i
        
        return []
        