from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Your frequency map (Perfect as it is)
        hashS = {}
        for i in range(len(nums)):
            hashS[nums[i]] = 1 + hashS.get(nums[i], 0)
            
        answer = []
        
        # 2. Loop 'k' times to find the top 'k' elements
        for _ in range(k):
            best_freq = -1
            best_num = None
            
            # Scan the dictionary to find the current most frequent number
            for num, freq in hashS.items():
                if freq > best_freq:
                    best_freq = freq
                    best_num = num
            
            # Append the actual NUMBER (key), not the frequency count
            answer.append(best_num)
            
            # "Delete" or reset this number's count so it isn't picked again
            hashS[best_num] = -1
            
        return answer
