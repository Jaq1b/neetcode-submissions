class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        e = {}
        for i in nums:
            e[i] = 1+e.get(i,0)

        answer = []
        for num,cnt in e.items():
            answer.append([cnt,num])
        answer.sort()

        res = []
        while len(res)<k:
            res.append(answer.pop()[1])
        return res
        
            
            
        
        
            
        
        
        