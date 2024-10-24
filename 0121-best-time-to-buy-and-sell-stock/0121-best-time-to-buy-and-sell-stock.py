class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # profit zero then pachi peli price buy ni
        # sell agar motu hoy buy karta to max of profit, replace baki profit
        # profit nanu hase ka negative hase to buy replace

        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit