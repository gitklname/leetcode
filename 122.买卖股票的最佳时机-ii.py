#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        state0, state1 = 0, -prices[0]
        for i in range(1, len(prices)):
            state0, state1 = max(state0, state1 + prices[i]), max(state0-prices[i], state1)
        
        return state0
# @lc code=end

