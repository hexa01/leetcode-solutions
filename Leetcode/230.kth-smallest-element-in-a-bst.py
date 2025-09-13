#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap =  []
        def bfs(node):
            if node:
                if len(heap) < k:
                    heapq.heappush(heap,-node.val)
                elif -node.val > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,-node.val)
                if not node.left and not node.right:
                    return 
                bfs(node.left)
                bfs(node.right)
        bfs(root)
        return -heap[0]
        
# @lc code=end

