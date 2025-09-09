#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged = []
        merged.append(intervals[0])
        for i in range(1,len(intervals)):
                if merged[-1][1] >= intervals[i][0]: #overlap
                    merged[-1][1] = max(merged[-1][1],intervals[i][1])
                else:
                    merged.append(intervals[i])  #no overlap
        return merged
        
# @lc code=end

