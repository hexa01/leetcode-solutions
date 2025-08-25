#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if total_sum -left_sum - nums[i] == left_sum:
                return i
            left_sum = left_sum + nums[i]
        return -1
        
# @lc code=end

