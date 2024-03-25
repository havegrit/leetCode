class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDate = 0
        sellDate = 0
        totalProfit = 0
        maxProfit = 0
        cnt = 0

        for i in range(len(prices)-1):
            buyDate = 0
            cnt += 1
            sellDate = cnt
            if prices[buyDate] < prices[sellDate]:
                totalProfit += prices[sellDate] - prices[buyDate]
            for j in range(i + 1, len(prices)):
                buyDate = sellDate
                sellDate = j
                if prices[buyDate] >= prices[sellDate]:
                    continue
                totalProfit += prices[sellDate] - prices[buyDate]
            sellDate = 0
            if totalProfit > maxProfit:
                maxProfit = totalProfit
            totalProfit = 0

        return maxProfit
