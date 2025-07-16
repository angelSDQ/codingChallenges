/**
 * LeetCode-style Problem (Easy-Medium): Filter Numbers Outside a Range
 *
 * Given an array of integers nums, and two integers low and high,
 * return a new array containing only the numbers that are *strictly outside the range (low, high)*,
 * in the same order as they appear in the original array.
 *
 * Parameters:
 * - int[] nums: A non-empty array of integers
 * - int low: The lower bound of the range (exclusive)
 * - int high: The upper bound of the range (exclusive)
 *
 * Returns:
 * - int[]: An array of integers from the input array that lie outside the exclusive range (low, high)
 *
 * Examples:
 * Input: nums = [1, 5, 10, 15, 20], low = 5, high = 15  
 * Output: [1, 20]
 *
 * Input: nums = [-10, -5, 0, 5, 10], low = -5, high = 5  
 * Output: [-10, 10]
 *
 * Input: nums = [100, 200, 300], low = 0, high = 500  
 * Output: []
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^6 <= nums[i], low, high <= 10^6
 * - low < high
 */

// create a function called numsNotInRange() passing in 3 parameters nums, low, high (these last two are inclusive)
// function numdNotInRange(nums, low, high) {
//      create a variable lowAndHigh of let type set to []
//      let notInRange = []; 
//      use a for loop to iterate on nums like this --> (let num of nums)
//      for (let num of nums) {
//          use an if statement to find the low and high numbers condition
//          if (num < low || num > high) {
//              lowAndHigh.push(num);
        //return lowAndHigh;

        function numsNotInRange(nums, low, high) {
            let notInRange = [];
            for (let num of nums) {
                if (num < low || num > high) {
                    notInRange.push(num);
                }
            }
            return notInRange;
        }
        
        console.log(numsNotInRange([1, 5, 10, 15, 20], 5, 15));