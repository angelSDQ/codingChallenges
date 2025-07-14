// * LeetCode-style Problem: Square Each Number
//  *
//  * Given an array of integers `nums`, return a new array where each element
//  * is the square of the corresponding element in the input array.
//  *
//  * Parameters:
//  * int[] nums - a non-empty array of integers
//  *
//  * Returns:
//  * int[] - an array containing the squares of the input numbers
//  *
//  * Examples:
//  * Input: nums = [1, 2, 3, 4]
//  * Output: [1, 4, 9, 16]
//  *
//  * Input: nums = [-1, -2, -3]
//  * Output: [1, 4, 9]
//  *
//  * Input: nums = [0]
//  * Output: [0]
//  *
//  * Constraints:
//  * - 1 <= nums.length <= 10^4
//  * - -10^3 <= nums[i] <= 10^3
//  */

// create a function called squareNums passing 1 parameter nums
// function squareNums(nums) {
//      declare a variable a variable called squaredR let type and set to []   
//      let squaredR = [];
//      use a for loop to iterate on nums
//      for (let i = 0; i < nums.length; i++) {
//          use Math.pow( to raise the number times, pass (nums[i], 2). Use .push() to add all numbers into squaredR
//          squaredR.push(Math.pow(nums[i], 2));  
//      }
//      return squaredArray;
//}

function squareNums(nums) {
    let squaredR = [];
    for (let num of nums) {
        squaredR.push(Math.pow(num, 2));   
    }
    return squaredR;
}

console.log(squareNums([-1, -2, -3, 4]));