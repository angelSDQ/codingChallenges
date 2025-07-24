#  * LeetCode-style Problem (Easy-Medium): Find Common Elements in Two Arrays
#  *
#  * Given two arrays of integers nums1 and nums2, return a new array containing 
#  * all the unique numbers that appear in both arrays. The result can be returned 
#  * in any order.
#  *
#  * Parameters:
#  * - int[] nums1: A non-empty array of integers
#  * - int[] nums2: A non-empty array of integers
#  *
#  * Returns:
#  * - int[]: An array of integers that are common to both nums1 and nums2, with no duplicates
#  *
#  * Examples:
#  * Input: nums1 = [1, 2, 2, 3], nums2 = [2, 3, 4]  
#  * Output: [2, 3]
#  *
#  * Input: nums1 = [4, 5, 6], nums2 = [1, 2, 3]  
#  * Output: []
#  *
#  * Input: nums1 = [1, 1, 1], nums2 = [1, 1]  
#  * Output: [1]
#  *
#  * Constraints:
#  * - 1 <= nums1.length, nums2.length <= 10^4
#  * - -10^6 <= nums1[i], nums2[i] <= 10^6

# define a function findingMatchingNumsInArray() passing 2 parameters nums1 and nums2
# def findingMatchingNumsInArray(nums1, nums2):
#   declare an empty set
#   matchesFound = set()
#   commonNums = []
#   use a for in loop to iterate on nums1
#   for num in nums1:
#       use an if statement to check for the condition --> num in nums2
#       if num in nums2:
#           when true populate matchesFound using .append()
#           matchesFound(matchesFound.add(num))
#   return matchesFound


def findingMatchingNumsInArray(nums1, nums2):
    matchesFound = set()
    for num in nums1:
        if num in nums2:
            matchesFound.add(num)
    return list(matchesFound)

print(findingMatchingNumsInArray([1, 1, 1, 2, 2], [1, 1, 2, 2]))