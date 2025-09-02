#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        visited_index = set()
        def getIndex(index,direction):
            next_index = (index + nums[index]) % n
            next_direction = 1 if nums[next_index] > 0 else -1
            if direction != next_direction or index == next_index:
                return -1
            return next_index

        for i in range(n):
            if i in visited_index:
                continue
            slow = i
            fast = i
            direction = 1 if nums[i] > 0 else -1
            while True:
                visited_index.add(slow)
                visited_index.add(fast)
                slow = getIndex(slow,direction)
                fast = getIndex(fast,direction)
                if slow == -1 or fast == -1:
                    break

                fast = getIndex(fast,direction)
                if fast == -1:
                    break
                if slow == fast:
                    return True   
        return False
# @lc code=end

