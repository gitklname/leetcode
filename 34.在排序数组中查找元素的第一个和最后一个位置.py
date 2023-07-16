#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bisearchL(arr: list, target) -> int:
            left, right = 0, len(arr) - 1
            
            while(left <= right):
                mid = left + (right - left) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                elif arr[mid] == target:
                    right = mid - 1
            
            if left >= len(arr):
                return -1
            return left if arr[left]==target else -1

        def bisearchR(arr: list, target) -> int:
            left, right = 0, len(arr) - 1
            
            while(left <= right):
                mid = left + (right - left) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                elif arr[mid] == target:
                    left = mid + 1
            
            if right < 0:
                return -1
            return right if arr[right]==target else -1
        
        return [bisearchL(nums, target), bisearchR(nums, target)]
# @lc code=end

