#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_of_nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            list_of_nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        return list_of_nodes
        
# @lc code=end

