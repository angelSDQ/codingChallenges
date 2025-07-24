/**
 * LeetCode-style Problem (Easy-Medium): Check for Unique Elements in an Array
 *
 * Given an integer array `nums`, determine whether all elements in the array are unique.
 * Return `true` if no element appears more than once; otherwise, return `false`.
 *
 * Your task is to write a function that checks for duplicate elements in the array.
 *
 * Parameters:
 * - int[] nums: a non-empty array of integers
 *
 * Returns:
 * - boolean: `true` if all elements are unique, `false` if there are duplicates
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4]
 * Output: true
 *
 * Input: nums = [1, 2, 2, 3]
 * Output: false
 *
 * Input: nums = [10]
 * Output: true
 *
 * Constraints:
 * - 1 <= nums.length <= 10^5
 * - -10^9 <= nums[i] <= 10^9
 */


// create a function findDuplicates() passing nums
// function findDuplicates(nums) {
//      create an empty list uniqueNums
//      let uniqueNums = [];
//      use a let of loop to iterate on nums
//      for (let num of nums) {
//          use an if statement to check the condition uniqueNums.inclcudes(num)
//          if uniqueNums.inclcudes(num) {
//                  return false
//          }
//          uniqueNums.add(num)
//      }
//      return true
// }

function findDuplicates(nums) {
    let uniqueNums = [];
    for (let num of nums) {
        if (uniqueNums.includes(num)) {
            return false
        }
        uniqueNums.push(num)
    }
    return true
}

console.log(findDuplicates([1, 2, 3, 4]));