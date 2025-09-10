#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0 
        intervals.sort(key = lambda x: x[1]) #sort by second number
        prev_end = -5 * 10**4 - 1  #lowest value of intervals can have by constraint
        for start,end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                count += 1
        return count
        
# @lc code=end

