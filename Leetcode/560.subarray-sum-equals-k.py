#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = []
        n = len(nums)
        prefix_sum.append(nums[0])
        for i in range(1,n):
            prefix_sum.append(prefix_sum[i-1] + nums[i])
        count = 0
        dict = {}
        for i in range(n):
            if prefix_sum[i] == k:
                count +=1
            key = prefix_sum[i] - k
            count = count + dict.get(key,0)
            dict[prefix_sum[i]] = dict.get(prefix_sum[i],0) + 1
        return count
            
        
        
# @lc code=end

