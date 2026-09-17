class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # create a set filled with the values of num
        longest = 0 # longest tracker

        for num in numSet: # loops through the set
            if (num - 1) not in numSet: # if the lower value is not in the set
                length = 1 # reset length
                while (num + length) in numSet: #while num + length in numest, this checks for sequence
                    length += 1 # length+=1
                longest = max(length, longest) # catch longest
        return longest # return longest