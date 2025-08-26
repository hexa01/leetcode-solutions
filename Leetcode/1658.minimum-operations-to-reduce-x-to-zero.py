#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum = 0
        max_window = -1
        left = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_window = max(max_window, right - left + 1)

        return len(nums) - max_window if max_window != -1 else -1
        
# @lc code=end

