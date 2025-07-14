/*
 * LeetCode-style Problem: Double Odd Numbers
 *
 * Given an array of integers `nums`, return a new array where each odd number
 * is doubled and each even number remains the same.
 *
 * Parameters:
 * int[] nums - a non-empty array of integers
 *
 * Returns:
 * int[] - an array where odd numbers are doubled, and even numbers stay unchanged
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4]
 * Output: [2, 2, 6, 4]
 *
 * Input: nums = [0, -1, -2, 5]
 * Output: [0, -2, -2, 10]
 *
 * Input: nums = [8, 7, 6]
 * Output: [8, 14, 6]
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^6 <= nums[i] <= 10^6
 */

// create a function doublingEvens() passing in one parameter nums
// function doublingEvens(nums) {
//      create a variable doubledOddNums of let type set to []
//      let doubledOddNums  = []
//      use a for loop to iterate on nums(parameter)
//      for (let num of nums) {
//          use an if statement to check the condition num % 2 == 1 || num % 2 == -1 we want to divide the numbers by 2 if its an odd number
//          if (nums[i] % 2 == 1 || num % 2 == -1) {
//              when true the odd number will be doubled or multiplied by 2 num * 2 use .push to add the elements to modifiedNums
//              modifiedNums.push(num * 2);
//          } else {
//                  modifiedNums.push(num)
//          }
//      return modifiedNums;
// }

function doublingEvens(nums) {
    let modifiedNums  = []
    for (let num of nums) {
        if (num % 2 == 1 || num % 2 == -1) {
            modifiedNums.push(num * 2);
        } else {
            modifiedNums.push(num)
        }
    }
    return modifiedNums;
}

console.log(doublingEvens([8, 7, 6]));