class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy: int = 0
        profit: int = 0

        for sell in range(1, len(prices)):
            if (prices[buy] < prices[sell]):
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
        
        return profit