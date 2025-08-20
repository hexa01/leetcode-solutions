#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def helper(i,current):
            if i == len(nums):
                result.append(current)
                return
            not_pick = current      
            pick = current + [nums[i]]  
            helper(i+1,not_pick)
            helper(i+1,pick)
        helper(0,[])
        return result

# @lc code=end

