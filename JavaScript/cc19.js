/**
 * LeetCode-style Problem (Easy): Check if Target Exists in Array
 *
 * Given an array of integers `nums` and an integer `target`, return true if the target
 * exists in the array, and false otherwise.
 *
 * Parameters:
 * - int[] nums: A non-empty array of integers
 * - int target: The integer to search for
 *
 * Returns:
 * - boolean: true if target exists in nums, false otherwise
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4, 5], target = 3  
 * Output: true
 *
 * Input: nums = [10, 20, 30], target = 25  
 * Output: false
 *
 * Input: nums = [-5, -2, 0, 2, 5], target = -2  
 * Output: true
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^6 <= nums[i], target <= 10^6
 */

// create a function findingTargetNum() passing in 2 parameters (nums, target)
// function findingTargetNum(nums, target) {
//      use a for of loop to iterate on nums 
//      for (let num of nums) {
//          use an if statement to check the condition num 
//          if (num === target) {
//              return true;
//          }
//      }
//      return false;
// }        


function findingTargetNum(nums, target) {
    // for (let num of nums) {
        if (nums.includes(target)) {
            console.log(nums)
            return true;
        }
    // }
    return false;
}   

console.log(findingTargetNum([1, 2, 3, 4, 5], 6));