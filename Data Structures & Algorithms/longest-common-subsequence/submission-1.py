class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1] * n for _ in range(m)]

        def func(i,j):
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + func(i+1,j+1)

            else:
                dp[i][j] = max(func(i+1,j),func(i,j+1),func(i+1,j+1))

            return dp[i][j]


        return func(0,0)