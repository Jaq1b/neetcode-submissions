class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        e = {}

        for num in nums:
            e[num] = 1 + e.get(num,0)
        arr = []
        for n,c in e.items():
            arr.append([c,n])
        arr.sort()
        
        ans = []
        while len(ans)<k:
            ans.append(arr.pop()[1])
        return(ans)
            

       
    
       

        


        