#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        state0, state1 = 0, -prices[0]
        for i in range(1, len(prices)):
            state0 = max(state0, state1 + prices[i])
            state1 = max(-prices[i], state1)
        
        return state0
# @lc code=end

