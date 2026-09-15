class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        differences = []
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                differences.append(prices[j]-prices[i])
        
        differences.sort()
        return differences[-1]


        