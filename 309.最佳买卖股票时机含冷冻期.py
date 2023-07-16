#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        cool=1
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            if i == 1:
                dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
                dp[1][1] = max(dp[0][1], -prices[1])
                continue
        
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) 
            dp[i][1] = max(dp[i-1-cool][0] - prices[i], dp[i-1][1])
        
        return dp[n-1][0]
# @lc code=end

