#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter_ = Counter(nums)
        counter_ = Counter(dict(sorted(counter_.items(), key=lambda item: item[0])))

        n = len(counter_)
        dp = [0] * n
        key0 = list(counter_.keys())[0]
        if len(counter_) == 1:
            return key0 * counter_[key0]
        key1 = list(counter_.keys())[1]
        for i in range(0, n):
            if i == 0:
                dp[i] = key0 * counter_[key0]
            elif i == 1:
                if (key1 == key0 + 1):
                    dp[i] = max(key0 * counter_[key0], key1 * counter_[key1])
                else: 
                    dp[i] = key0 * counter_[key0] + key1 * counter_[key1]
            else:
                if (list(counter_.keys())[i] == list(counter_.keys())[i-1] + 1):
                    dp[i] = max(list(counter_.keys())[i] * counter_[list(counter_.keys())[i]] + dp[i-2], dp[i-1])
                else:
                    dp[i] = list(counter_.keys())[i] * counter_[list(counter_.keys())[i]] + dp[i-1]
        return dp[-1]
# @lc code=end

