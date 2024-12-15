class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        i=0
        for j in range(len(prices)-1):
            j+=1
            if prices[i]<prices[j]:
                max_profit = max(max_profit, prices[j]-prices[i])
            elif prices[j]<prices[i]:
                i=j
        return max_profit
