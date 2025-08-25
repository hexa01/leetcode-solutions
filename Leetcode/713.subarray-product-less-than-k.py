#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        product = 1
        count = 0
        if k <= 1:
            return 0
        for right in range(len(nums)):
            product = product * nums[right]
            while product >= k:
                product = product // nums[left]
                left = left + 1
            count += ( right - left) + 1
        return count
# @lc code=end

