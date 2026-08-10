class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = list(range(2))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer[0]=i
                    answer[1]=j
                else:
                
                    continue
        return answer