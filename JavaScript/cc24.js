/**
 * LeetCode-style Problem (Easy): Check if All Elements Are the Same
 *
 * Given an integer array `nums`, determine whether **all elements in the array are the same**.
 * Return `true` if every element is equal to the first one; otherwise, return `false`.
 *
 * Parameters:
 * - int[] nums: a non-empty array of integers
 *
 * Returns:
 * - boolean: true if all elements in the array are equal, false otherwise
 *
 * Examples:
 * Input: nums = [2, 2, 2, 2]
 * Output: true
 *
 * Input: nums = [1, 2, 1]
 * Output: false
 *
 * Input: nums = [7]
 * Output: true
 *
 * Constraints:
 * - 1 <= nums.length <= 10^5
 * - -10^9 <= nums[i] <= 10^9
 */


//create a function findAllDuplicates() passing 1 parameter int[] nums
//function findAllDuplicates(nums) {
//      declare an empty list duplicateNums set to []
//      let duplicateNums = [];
//      use a let of loop to iterate on nums
//      for (let num of nums) {
//          use an if statement to check for the condition
//          if (duplicateNums.includes(num)) {
//              return false;
//          }
//          duplicateNums.push(num);     
//      }
//      return true;
//  }

function findAllDuplicates(nums) {
    let duplicateNums = [nums[0]];
    for (let i = 1; i < nums.length; i++) {
        if (!(duplicateNums.includes(nums[i]))) {
            console.log(duplicateNums);
            return false;
        }
        duplicateNums.push(nums[i]);     
    }
    return true;
}

console.log(findAllDuplicates([2, 2, 2, 2]));