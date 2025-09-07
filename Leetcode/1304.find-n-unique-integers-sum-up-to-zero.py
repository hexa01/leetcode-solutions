#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n % 2 != 0:
            arr.append(0)
            n -= 1 
        while n > 0:
            arr.append(n)
            arr.append(-(n))
            n -= 2
        return arr
        
# @lc code=end

