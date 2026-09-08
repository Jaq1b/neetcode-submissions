class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        l = 0
        r = len(nums) - 1
        count = 1
        best = 1
        while l < r:
            if (nums[l+1] - nums[l]) > 1:
                count = 1
            elif (nums[l+1] - nums[l]) == 1:
                count += 1
            l += 1
            best = max(best, count)

        return best