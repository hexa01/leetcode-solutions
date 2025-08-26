#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        curr_sum = 0
        n = len(nums)
        result = [-1 for i in range(n)]
        if k == 0:
            return nums
        left = 0
        for right in range(n):
            curr_sum += nums[right]
            if right >= 2*k:
                result[right-k] = curr_sum // (2*k + 1)
                curr_sum -= nums[left]
                left+= 1
        return result

# @lc code=end

