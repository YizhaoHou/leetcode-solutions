class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in reversed(range(len(prices))):
            if i == 0:
                prices[i] = 0
            else:
                prices[i] = prices[i] - prices[i - 1]

        maxsell = [0]
        for i in range(1,len(prices)):
            sell = max(prices[i], maxsell[i - 1] + prices[i])
            maxsell.append(sell)
        if max(maxsell) <= 0:
            return 0
        else:
            return max(maxsell)