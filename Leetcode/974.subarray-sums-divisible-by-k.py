#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        curr_sum = 0
        dict = {0:1}
        for j in range(len(nums)):
            curr_sum += nums[j]
            curr_sum %= k
            count += dict.get(curr_sum,0)
            dict[curr_sum]= dict.get(curr_sum,0) + 1
        return count
        
        
# @lc code=end

