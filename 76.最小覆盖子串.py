#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m:
            return ''
        
        count = defaultdict(int)

        for c in t:
            count[c] += 1
        
        def check(count):
            for c in count:
                if count[c] > 0:
                    return False
            
            return True
        
        left, right = 0, -1
        minlen = float('inf')
        min_l, min_r = -1, -1

        while right < n-1:
            right += 1
            count[s[right]] -= 1
            while check(count) and left <= right:
                if minlen > right-left+1:
                    minlen = right-left+1
                    min_l, min_r = left, right
                count[s[left]] += 1
                left += 1
        
        return s[min_l:min_r+1] if min_l != -1 else ''


# @lc code=end

