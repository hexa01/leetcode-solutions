#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        def is_32bit(a, b):
            return (a * 10 + b <= 2**31 - 1)
        dup_x = abs(x)
        reverse = 0
        while dup_x > 0:
            last = dup_x % 10
            if is_32bit(reverse, last):
                reverse = reverse * 10 + last
            else:
                return 0
            dup_x //= 10
        if x < 0:
            return -reverse
        else:
            return reverse
        
# @lc code=end

