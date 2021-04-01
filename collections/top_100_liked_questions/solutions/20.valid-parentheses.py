#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')':'(',']':'[','}':'{'}
        for p in s:
            if p in valid.values():
                stack.append(p)
            elif not stack or valid[p] != stack.pop():
                return False 
        return not stack 
# @lc code=end
