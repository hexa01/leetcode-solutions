#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool: 
        dict = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_sum %= k
            if prefix_sum in dict:
                if i - dict[prefix_sum] >= 2:
                    return True
            else:
                dict[prefix_sum] = i
        return False
