#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [ [[0]*3 for _ in range(2)] for _ in range(n)]
        for i in range(n):
            for k in range(2, 0, -1):
                if i==0:
                    dp[i][0][k] = 0
                    dp[i][1][k] = -prices[i]
                    continue
                dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][1][k] + prices[i]) 
                dp[i][1][k] = max(dp[i-1][0][k-1] - prices[i], dp[i-1][1][k])
        
        return dp[n-1][0][2]
# @lc code=end

