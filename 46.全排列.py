#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return [nums]
        used = [False] * n
        path = []
        res = []

        def backtrack(nums, path, used):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(nums, path, used)
                path.pop()
                used[i] = False
        
        backtrack(nums, path, used)
        return res
# @lc code=end

