/**
 * LeetCode-style Problem (Easy-Medium): Filter Numbers Whose Squares Are Less Than a Given Value
 *
 * Given an array of integers `nums` and a single integer `limit`,
 * return a new array containing only the numbers from `nums` whose squares are strictly less than `limit`,
 * in the same order as they appear in the original array.
 *
 * Parameters:
 * - int[] nums: A non-empty array of integers
 * - int limit: A positive integer to compare against the square of each number
 *
 * Returns:
 * - int[]: An array of integers from the input array whose squares are < limit
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4, 5], limit = 10  
 * Output: [1, 2, 3]  // because 1^2=1, 2^2=4, 3^2=9 are all < 10
 *
 * Input: nums = [-5, -2, 0, 2, 5], limit = 25  
 * Output: [-2, 0, 2]  // because (-2)^2=4, 0^2=0, 2^2=4 are all < 25
 *
 * Input: nums = [10, 20, 30], limit = 50  
 * Output: [10]  // 10^2=100 is not < 50, so result is []
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^3 <= nums[i] <= 10^3
 * - 1 <= limit <= 10^6
 */

// create a function findNumSquaredLessThanLimit() passing in 2 parameters nums and limit
// function findNumSquaredLessThanLimit(nums, limit) {
//      create a variable numsLessThanLimit of let type set to []
//      let numsLessThanLimit = []
//      use a for loop to iterate on nums
//      for (let num of nums) {
//          create a local variable numSquared of let type and set to (num * 2)
//          let numSquared = (num * 2);
//          use an if statement to check for the condition (numSquared < limit) 
//          if (numSquared < limit) {
//              if true use .push() to populate numsLessThanLimit
//              numsLessThanLimit.add(num);
//          }
//      }
//      return numsLessThanLimit
// }


function findNumSquaredLessThanLimit(nums, limit) {
    let numsLessThanLimit = [];
    for (let num of nums) {
        if (Math.pow(num, 2) < limit) {
            numsLessThanLimit.push(num);
        }
    }
    return numsLessThanLimit
}

console.log(findNumSquaredLessThanLimit([-5, -2, 0, 2, 5], 25));