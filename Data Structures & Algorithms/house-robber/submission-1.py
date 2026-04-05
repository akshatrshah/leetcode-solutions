class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def func(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            a = nums[i] + func(i+2)
            b = func(i+1)
            dp[i] = max(a,b)
            return dp[i]
        
        return max(func(0),func(1))