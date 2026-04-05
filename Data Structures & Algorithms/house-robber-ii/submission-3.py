class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(arr):
            if len(arr) == 1:
                return arr[0]
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])

            for i in range(2,len(arr)):
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        return max(func(nums[1:]),func(nums[:n-1]))

