#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        prev,sum,finalSum =  0,0,0
        for i in range(len(nums)):
            if nums[i] > prev:
                sum += nums[i]
            else:
                finalSum = max(finalSum,sum)
                sum = nums[i]
            prev = nums[i]
        return max(sum,finalSum)
# @lc code=end

