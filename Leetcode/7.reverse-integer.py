#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        def is_32bit(a, b, negative=False):
            if negative:
                return a < (-INT_MIN) // 10 or (a == (-INT_MIN) // 10 and b <= (-INT_MIN) % 10)
            else:
                return a < INT_MAX // 10 or (a == INT_MAX // 10 and b <= INT_MAX % 10)

        dup_x = abs(x)
        reverse = 0
        negative = x < 0

        while dup_x > 0:
            last = dup_x % 10
            if not is_32bit(reverse, last, negative):
                return 0
            reverse = reverse * 10 + last
            dup_x //= 10

        return -reverse if negative else reverse
        
# @lc code=end

