class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    array.append(i)
                    array.append(j)
        return array