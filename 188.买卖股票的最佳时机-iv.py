#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        maxk = k
        if k > n//2:
            maxk = n//2
        dp = [ [[0]*(maxk+1) for _ in range(2)] for _ in range(n)]

        for i in range(n):
            for l in range(maxk, 0, -1):
                if i==0:
                    dp[i][0][l] = 0
                    dp[i][1][l] = -prices[i]
                    continue
                dp[i][0][l] = max(dp[i-1][0][l], dp[i-1][1][l] + prices[i]) 
                dp[i][1][l] = max(dp[i-1][0][l-1] - prices[i], dp[i-1][1][l])
        
        return dp[n-1][0][maxk]
# @lc code=end

