#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        op = []
        curr = ''
        def preorder_traversal(node,path):
            if node:
                if path:
                    path += '->' + str(node.val)
                if not path:
                    path = str(root.val)
                if not node.left and not node.right:
                    op.append(path)
                preorder_traversal(node.left, path)
                preorder_traversal(node.right,path)
        preorder_traversal(root,'')
        return op
        
# @lc code=end

