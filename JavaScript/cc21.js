/**
 * LeetCode-style Problem (Easy-Medium): Find Non-Common Elements Between Two Arrays
 *
 * Given two integer arrays nums1 and nums2, return a new array containing all the unique
 * numbers that appear in only one of the two arrays (i.e., not shared between them).
 * The result should not contain duplicates, and the order of elements does not matter.
 *
 * Parameters:
 * - int[] nums1: A non-empty array of integers
 * - int[] nums2: A non-empty array of integers
 *
 * Returns:
 * - int[]: An array of integers that are unique to either nums1 or nums2 (but not both)
 *
 * Examples:
 * Input: nums1 = [1, 2, 3], nums2 = [2, 3, 4]  
 * Output: [1, 4]
 *
 * Input: nums1 = [5, 6, 7], nums2 = [7, 8, 9]  
 * Output: [5, 6, 8, 9]
 *
 * Input: nums1 = [1, 1, 2], nums2 = [2, 3]  
 * Output: [1, 3]
 *
 * Constraints:
 * - 1 <= nums1.length, nums2.length <= 10^4
 * - -10^6 <= nums1[i], nums2[i] <= 10^6
 */

// create a function findsUniqueNums passing 2 parameters nums1 and nums2
// function findsUniqueNums(nums1, nums2) {
//      declare a variables
//      const uniqueNums = new Set();
//      use a for let of loop to iterate on nums1
//      for (let num of nums1) {
//          use an if statement to check the condition (nums2.includes(num)
//          if (nums2.includes(num)) {
//              when true populate uniqueNums using .add() passing in num
//              uniqueNums.add(num)
//          }
//      }
//      use a second for let of loop to iterate on nums2
//      for (let num of nums2) {
//          use an if statement to check the condition (nums1.includes(num)
//          if (nums1.includes(num)) {
//              when true populate uniqueNums using .add() passing in num
//              uniqueNums.add(num)
//          }
//      }
//      return Array.from(matchesFound);
//}

function findsUniqueNums(nums1, nums2) {
    const uniqueNums = new Set();
    for (let num of nums1) {
        if (!nums2.includes(num)) {
            uniqueNums.add(num)
        }
    }
    for (let num of nums2) {
        if (!nums1.includes(num)) {
            uniqueNums.add(num)
        }
    }
    return Array.from(uniqueNums);
}

function findsUniqueNums2(nums1, nums2) {
    const uniqueNums = new Set();
    for (let num of [...nums1, ...nums2]) {
        if (!(nums1.includes(num) && nums2.includes(num))) {
            uniqueNums.add(num);
        }
    }
    return Array.from(uniqueNums);
}

console.log(findsUniqueNums2([1, 2, 3], [2, 3, 4]))

