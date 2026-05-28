class Solution(object):
    def maxProfit(self, prices):
        minno = prices[0]
        profit = 0 
        for i in range(len(prices)):
            if prices[i]<minno:
                minno=prices[i]
            current_profit=prices[i]-minno 
            if current_profit>profit:
                profit=current_profit
        return profit
