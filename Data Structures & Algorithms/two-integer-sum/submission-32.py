class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        e = {} #hashmap for storing values

        for i,n in enumerate(nums):   #go through nums catching hte value and index
            diff = target - n #difference between value and target
            if diff in e:  # if difference in hashmap
                return [e[diff], i] #return index of curr and index of i
            e[n] = i #set e if it does not exist in hashmap
        return [] #return empty if none found
        