/**
 * LeetCode-style Problem (Easy-Medium): Find Common Elements in Two Arrays
 *
 * Given two arrays of integers nums1 and nums2, return a new array containing 
 * all the unique numbers that appear in both arrays. The result can be returned 
 * in any order.
 *
 * Parameters:
 * - int[] nums1: A non-empty array of integers
 * - int[] nums2: A non-empty array of integers
 *
 * Returns:
 * - int[]: An array of integers that are common to both nums1 and nums2, with no duplicates
 *
 * Examples:
 * Input: nums1 = [1, 2, 2, 3], nums2 = [2, 3, 4]  
 * Output: [2, 3]
 *
 * Input: nums1 = [4, 5, 6], nums2 = [1, 2, 3]  
 * Output: []
 *
 * Input: nums1 = [1, 1, 1], nums2 = [1, 1]  
 * Output: [1]
 *
 * Constraints:
 * - 1 <= nums1.length, nums2.length <= 10^4
 * - -10^6 <= nums1[i], nums2[i] <= 10^6
 */

//create a function findingMatchingNumsInArray() passing 2 parameters nums1 and nums2
//function findingMatchingNumsInArray(nums1, nums2) {
//     declare a variable of set type
//     const matchesFound = new Set();
//     use a let of loop to iterate on nums1
//     for (let num of nums1) {
//          use an if statement to check for the condition (nums2, nums)
//          if (nums2, num) {
//              when true populate matchesFound using .push()
//                  matchesFound.push(num)
//                  const commonNumsInArrays = Array.from(matchesFound); 
//          }
//     }
//     return commonNumsInArrays;



function findingMatchingNumsInArray(nums1, nums2) {
    const matchesFound = new Set();
    for (let num of nums1) {
        if (nums2.includes(num)) {
            matchesFound.add(num)
        }
    }
    return Array.from(matchesFound);

}

console.log(findingMatchingNumsInArray([1, 1, 1], [1, 1]))