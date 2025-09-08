#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i], 0) + 1
            
        heap = []
        for num, count in dict.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]
        
# @lc code=end

