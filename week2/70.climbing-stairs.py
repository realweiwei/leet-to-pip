#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (53.31%)
# Likes:    22830
# Dislikes: 931
# Total Accepted:    4M
# Total Submissions: 7.5M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp(i) denotes the number of ways to climb to ith step
        # The problem is asking about dp(n)
        # You can take 1 or 2 steps, so dp(i) = dp(i-1) + dp(i-2)
        dp = [0] * n
        for i in range(n):
            # dp(1)
            if i == 0:
                dp[i] = 1
            # dp(2)
            elif i == 1:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]
        # dp(n)
        return dp[n-1]
        
# @lc code=end

