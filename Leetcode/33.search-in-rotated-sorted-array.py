#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #modified binary search
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid =(left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
       
# @lc code=end

