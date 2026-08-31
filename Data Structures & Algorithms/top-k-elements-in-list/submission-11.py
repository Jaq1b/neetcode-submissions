class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e = defaultdict(int)
       
    
        for num in nums:
            if num in e:
                e[num] +=1
            else:
                e[num] = 1
        answer = []
        for r in range(k):
                top_key = max(e, key = e.get)
                answer.append(top_key)
                e.pop(top_key)
               
        return answer
        