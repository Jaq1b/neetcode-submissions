class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        best = 1
        l = 0
        r = 1
        sequence = 1
        while r < len(nums):
            if nums[r] - nums[l] == 1:
                sequence += 1
                l += 1
                r += 1
            elif nums[r] - nums[l] == 0:
                l += 1
                r += 1
            else:
                l = r
                r += 1
                sequence = 1
            best = max(best, sequence)

        return best