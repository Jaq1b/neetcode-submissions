class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        e = {}
        for num in range(len(nums)):
            diff = target - nums[num]
            if diff in e:
                return [e[diff],num]
            e[nums[num]] = num
        return []
                       

       