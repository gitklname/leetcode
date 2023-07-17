#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        left, right = 0, 0
        res = 0

        for i, c in enumerate(s):
            count[c] += 1
            if i == 0:
                res = 1
                continue
            right = i
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res

# @lc code=end

