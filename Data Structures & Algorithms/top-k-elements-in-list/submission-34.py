class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e = {}
        for i in nums:
            e[i] = 1+(e.get(i,0))
        
        arr = []
        for i,n in e.items():
            arr.append([n,i])
        arr.sort()
        
        ans = []
        while k>0:
            ans.append(arr.pop()[1])
            k-=1

        return ans