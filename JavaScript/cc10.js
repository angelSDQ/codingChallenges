/**
 * LeetCode-style Problem: Reverse a List
 *
 * Given a list of integers `nums`, return the list in reversed order.
 *
 * Examples:
 * Input: nums = [1, 2, 3]
 * Output: [3, 2, 1]
 *
 * Input: nums = [5]
 * Output: [5]
 * Input: nums = [4, 8, 15, 16, 23, 42]
 * Output: [42, 23, 16, 15, 8, 4]
 *
 * Input: nums = [10, -1, 0, 7]
 * Output: [7, 0, -1, 10]
 *
 * Constraints:
 * - 1 <= nums.length <= 10^5
 * - -10^9 <= nums[i] <= 10^9
 * 
 */

// Declare a function called reversingNums() passing 1 parameter nums
// function reversingNums(nums) {
//     declare a variable numsReversed set equal to empty []
//     let numsReversed = [];
//     use a for loop to interate on numsReversed.length in reverse
//     for (let i = nums.length -1; i >= 0; i--) {
//         use .push passing nums[i] to populate numsReversed
//         numsReversed.push(nums[i]);
//     }
//     return numsReversed
//}

function reversingNums(nums) {
    let numsReversed = [];
    for (let i = nums.length -1; i >= 0; i--) {
        numsReversed.push(nums[i]);
    }
    return numsReversed;
}

console.log(reversingNums([4, 8, 15, 16, 23, 42]));

