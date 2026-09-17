class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e = {}

        for i in range(len(nums)):
            e[nums[i]] = 1 + e.get(nums[i],0)
        arr = []

        for i,n in e.items():
            arr.append([n,i])
        arr.sort()

        answer = []

        while k>0:
            answer.append(arr.pop()[1])
            k-=1
        return answer
        