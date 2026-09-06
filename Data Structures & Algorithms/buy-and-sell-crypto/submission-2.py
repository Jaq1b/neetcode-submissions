class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            
            for j in range(i, len(prices)):
                
                profit = (prices[j] - prices[i])
                
                if profit>best:
                    best = profit
        
        return best
        