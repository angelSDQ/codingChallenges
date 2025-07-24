/**
 * LeetCode-style Problem (Medium): Check if Two Arrays Are Permutations of Each Other
 *
 * Given two integer arrays `nums1` and `nums2`, determine whether one is a permutation of the other.
 * Two arrays are permutations of each other if they contain the same elements with the same frequencies,
 * regardless of order.
 *
 * Your task is to write a function that returns `true` if the arrays are permutations of each other,
 * and `false` otherwise.
 *
 * Parameters:
 * - int[] nums1: a non-empty array of integers
 * - int[] nums2: a non-empty array of integers
 *
 * Returns:
 * - boolean: true if nums1 is a permutation of nums2, false otherwise
 *
 * Examples:
 * Input: nums1 = [1, 2, 3], nums2 = [3, 2, 1]
 * Output: true
 *
 * Input: nums1 = [1, 2, 2], nums2 = [2, 1, 1]
 * Output: false
 *
 * Input: nums1 = [4, 5, 6], nums2 = [4, 6, 5]
 * Output: true
 *
 * Constraints:
 * - 1 <= nums1.length, nums2.length <= 10^4
 * - -10^6 <= nums1[i], nums2[i] <= 10^6
 */








// create a function findPermutation() passing 2 parameters nums1 and nums2
// function findPermutation(nums1, nums2) {
//      use an if statement to check if the length of nums1 and nums2 are the same
//      if (nums1.length != nums1.length) {
//          return false;
//      }
//      use a let of loop to iterate on nums1
//      for (let num of nums1) {
//          use an if statement to check if num if not in nums2
//          if (!num2.includes(num)) {
//              return false;
//          }
//      }
//      return true;
//}


function findPermutation(nums1, nums2) {
    if (nums1.length != nums1.length) {
        return false;
    }
    for (let num of nums1) {
        if (!nums2.includes(num)) {
            return false;
        }
        nums2 = removeTarget(nums2, num);
    }
    return true;
}

//create a function that tkes in an array and a number. 
//return an array without that number
function removeTarget(numArray, target) {
    let withoutTarget = []
    for (let num of numArray) {
        if (num != target){
            withoutTarget.push(num);
        }
    }
    return withoutTarget;
}



console.log(findPermutation([1, 1, 2], [2, 2, 1]))