class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        e = {}

        for num in nums:
            e[num] = 1+e.get(num,0)
        
        arr = []
        for c,n in e.items():
            arr.append([n,c])
        arr.sort()

        ans = []
        while len(ans)<k:
            ans.append(arr.pop()[1])
        return ans

       