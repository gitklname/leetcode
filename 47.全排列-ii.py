#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return [nums]
        used = [False] * n
        path = []
        res = []
        nums.sort()

        def backtrack(nums, path, used):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(nums, path, used)
                path.pop()
                used[i] = False
        
        backtrack(nums, path, used)
        return res
# @lc code=end

