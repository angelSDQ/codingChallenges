/*
 * LeetCode-style Problem: Raise Numbers to a Power
 *
 * Given an array of integers `nums` and an integer `exponent`, return a new array
 * where each element is raised to the power of `exponent`.
 *
 * Parameters:
 * int[] nums - a non-empty array of integers
 * int exponent - a non-negative integer representing the power to raise each number to
 *
 * Returns:
 * int[] - an array containing each number in `nums` raised to the power of `exponent`
 *
 * Examples:
 * Input: nums = [2, 3, 4], exponent = 2
 * Output: [4, 9, 16]
 *
 * Input: nums = [1, -1, 2], exponent = 3
 * Output: [1, -1, 8]
 *
 * Input: nums = [5], exponent = 0
 * Output: [1]
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^3 <= nums[i] <= 10^3
 * - 0 <= exponent <= 10
 */

// declare a function raisedToExponent() passing 2 parameters of int[] type nums and exponent
// function raisedToExponent(nums, exponent) {
//      declare a variable called raisedNums of let type and set to [] 
//      let squaredNums = [];
//      use a for loop to iterate on nums
//      for (let num of nums) {
//          now use the Math.pow() passing in nums and the exponent like this Math.pow(num, 2) and use .push to add them to squaredNums
//          squaredR.push(Math.pow(num, exponent)); 
//        }
//      return squaredNums;
//}




function raisedToExponent(nums, exponent) {
    let squaredNums = [];
    for (let num of nums) {
        squaredNums.push(Math.pow(num, exponent)); 
    }
    console.log(squaredNums);
    return squaredNums;
}

console.log(raisedToExponent([1, -1, 2], 3));