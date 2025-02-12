#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i in range (len(nums)):
            if nums[i] in dict_:
                return [dict_.get(nums[i]), i]
            else:
                dict_[target - nums[i]] = i
        return []

        
# @lc code=end

