#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        # Only track odd numbers
        size = n // 2
        is_prime = [True] * size
        is_prime[0] = False  # 1 is not prime

        # Upper limit for checking factors
        limit = int(n ** 0.5)
        for i in range(1, (limit // 2) + 1):
            if is_prime[i]:
                p = 2 * i + 1
                # Start marking at p*p
                start = (p * p) // 2
                for j in range(start, size, p):
                    is_prime[j] = False
        return sum(is_prime) + 1 #adding 1 because we are skipping 2, only even prime
        
# @lc code=end

