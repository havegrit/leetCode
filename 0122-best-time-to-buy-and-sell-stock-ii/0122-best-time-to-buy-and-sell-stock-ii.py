class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        days = len(prices)
        maxProfit = 0
        
        for i in range(days-1):
            if prices[i+1] > prices[i]:
                maxProfit += prices[i+1] - prices[i]
                
        return maxProfit
