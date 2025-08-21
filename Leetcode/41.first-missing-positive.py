#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            correct_pos = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        for j in range (len(nums)):
            if j + 1 != nums[j]:
                return j + 1
        return n + 1
        pass
# @lc code=end

