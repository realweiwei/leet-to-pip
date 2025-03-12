/*
 * @lc app=leetcode id=238 lang=java
 *
 * [238] Product of Array Except Self
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (67.36%)
 * Likes:    23813
 * Dislikes: 1527
 * Total Accepted:    3.4M
 * Total Submissions: 5.1M
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an integer array nums, return an array answer such that answer[i] is
 * equal to the product of all the elements of nums except nums[i].
 * 
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 * 
 * You must write an algorithm that runs in O(n) time and without using the
 * division operation.
 * 
 * 
 * Example 1:
 * Input: nums = [1,2,3,4]
 * Output: [24,12,8,6]
 * Example 2:
 * Input: nums = [-1,1,0,-3,3]
 * Output: [0,0,9,0,0]
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= nums.length <= 10^5
 * -30 <= nums[i] <= 30
 * The input is generated such that answer[i] is guaranteed to fit in a 32-bit
 * integer.
 * 
 * 
 * 
 * Follow up: Can you solve the problem in O(1) extra space complexity? (The
 * output array does not count as extra space for space complexity analysis.)
 * 
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] leftSoFar = new int[nums.length];
        int[] rightSoFar = new int[nums.length];
        int curr = 1;
        for (int i = 0; i < nums.length; i++) {
            curr *= nums[i];
            leftSoFar[i] = curr;
        }
        int rcurr = 1;
        for (int i = nums.length - 1; i > -1; i--) {
            rcurr *= nums[i];
            rightSoFar[i] = rcurr;
        }
        for (int i = 0; i < nums.length; i++) {
            int left = 1;
            int right = 1;
            if (i > 0) {
                left = leftSoFar[i - 1];
            }
            if (i < nums.length - 1) {
                right = rightSoFar[i + 1];
            }
            nums[i] = left * right;
        }
        return nums;
    }
}
// @lc code=end

