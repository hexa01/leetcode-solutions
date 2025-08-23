#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # highest power of 3 within constraint is 3^19 = 1162261467
        return n > 0 and 1162261467 % n == 0 
        
# @lc code=end

