#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def sum_of_squares(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        visited = set() #using hash, O(n) space complexity
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            n = self.sum_of_squares(n)
        return False
    
        
# @lc code=end

