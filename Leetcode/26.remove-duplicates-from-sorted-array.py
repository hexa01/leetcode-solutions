#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = 1
        for i in range(1, len(nums)):
            if (nums[i] != nums[i-1]):
                nums[n] = nums[i]
                n += 1
        return n


        pass
        
# @lc code=end

