class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1,len(dp)):
            for c in coins:
                if i - c >= 0:
                    coins_needed = 1 + dp[i-c]
                    dp[i] = min(dp[i],coins_needed)
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1