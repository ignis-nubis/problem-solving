#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) 
        while (lo < hi):
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid
            else:
                return mid
        return hi                
# @lc code=end
