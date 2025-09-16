#
# @lc app=leetcode id=2197 lang=python3
#
# [2197] Replace Non-Coprime Numbers in Array
#

# @lc code=start
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a,b):  #for finding GCD
            while b != 0:
                r = a % b
                if r == 0:
                    break
                else:
                    a = b
                    b = r
            return b
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            else:
                while stack:
                    g = gcd(stack[-1], num)
                    if g == 1:
                        break  # coprime, stop
                    num = stack.pop() * num // g  # replace with LCM
                stack.append(num)
        return stack
        
# @lc code=end

