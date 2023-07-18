#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(nums, target, n):
            _nums = sorted(nums)
            return _nSum(_nums, 0, len(nums)-1,target, n)

        def _nSum(nums, left, right, target, n):
            if n < 2 or (right - left + 1) < n:
                return []
            
            if n == 2:
                return twoSum(nums, left, right, target)
            
            res = []
            for i in range(left, right+1):
                if i > left and nums[i] == nums[i-1]:
                    continue
                tmp = _nSum(nums, i+1, right, target-nums[i], n-1)

                for ls in tmp:
                    res.append([nums[i]]+ls)
            return res

        def twoSum(nums, _left, _right, target):
            res = []
            left, right = _left, _right
            while left < right:
                if left > _left and nums[left]==nums[left-1]:
                    left += 1
                    continue
                if nums[left] + nums[right] == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
            return res
        
        return nSum(nums, target, 4)
# @lc code=end

