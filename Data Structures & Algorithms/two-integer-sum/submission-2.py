class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[i]+nums[j] == target and i != j:
                    array.append(i)
                    array.append(j)
                    array.sort()
                    return array
        return array
        
        