class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        buy = 0
        sell = 0

        while sell < len(prices):
            earn = prices[sell] - prices[buy]
            # print(earn)
            if earn >= 0:
                result = max(result, earn)
                sell = sell + 1
            else:
                buy = sell
                sell = sell + 1
        
        return result

        
        