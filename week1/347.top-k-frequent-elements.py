#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.96%)
# Likes:    17985
# Dislikes: 702
# Total Accepted:    2.6M
# Total Submissions: 4.1M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hacky way
        # counter = Counter(nums)
        # res = []
        # for [num, count] in counter.most_common(k):
        #     res.append(num)
        # return res
        
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        heap = [] # min heap
        for num, freq in counter.items(): 
            heapq.heappush(heap, [freq, num])
            if len(heap) > k: # if the heap's size > k, pop
                heapq.heappop(heap)
        res = [0] * k
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop(heap)[1]
        return res
        
# @lc code=end

