#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_index:
                return [num_index[diff], i]
            num_index[num] = i
        pass
# @lc code=end

