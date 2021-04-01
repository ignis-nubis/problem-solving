#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal diameter
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        diameter = 0
        dfs(root)
        return diameter
# @lc code=end
