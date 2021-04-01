#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
 
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
               return [hashmap[complement], i]
            hashmap[n] = i
# @lc code=end
