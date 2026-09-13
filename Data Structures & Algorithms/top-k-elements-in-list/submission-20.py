class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + (count.get(nums[i],0))
        ans = []
        for num, cnt in count.items():
            ans.append([cnt,num])
        ans.sort()

        res = []
        while len(res)<k:
            res.append(ans.pop()[1])
        return res