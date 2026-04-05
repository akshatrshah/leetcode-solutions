class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        def func(i):
            print(dp)
            if i >= n:
                return 0
            
            if dp[i] != 0:
                return dp[i]
            
            a = func(i+1)
            b = func(i+2)
            print(a,b)
            dp[i] = cost[i] + min(a,b)
            return dp[i]

        
        return min(func(0),func(1))