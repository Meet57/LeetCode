class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Making the number of coins to infinite
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # 0 coins for 0 value

        # Though it is sorted but this is an important step to build dp tree
        coins.sort()

        # putting all coins together to make the value as 11 requries 11, 1 coins
        for coin in coins:
            # coin less that the value cant be made
            for i in range(coin, amount + 1):
                # checking the current previous value is proper or if we use the current coin from above loop and substract it from the dp list returns the previous number with best coins and adding one as the coin it self
                # ex for 11, (11 one coins),(11 - 5 = best of 6 coins and using 5 coin so + 1)
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1