#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for i in nums: 
            if i in set_:
                return True
            else:
                set_.add(i)
        return False
# @lc code=end

