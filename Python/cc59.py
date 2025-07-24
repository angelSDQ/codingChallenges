# /**
#  * LeetCode-style Problem (Medium): Check if Two Arrays Are Permutations of Each Other
#  *
#  * Given two integer arrays `nums1` and `nums2`, determine whether one is a permutation of the other.
#  * Two arrays are permutations of each other if they contain the same elements with the same frequencies,
#  * regardless of order.
#  *
#  * Your task is to write a function that returns `true` if the arrays are permutations of each other,
#  * and `false` otherwise.
#  *
#  * Parameters:
#  * - int[] nums1: a non-empty array of integers
#  * - int[] nums2: a non-empty array of integers
#  *
#  * Returns:
#  * - boolean: true if nums1 is a permutation of nums2, false otherwise
#  *
#  * Examples:
#  * Input: nums1 = [1, 2, 3], nums2 = [3, 2, 1]
#  * Output: true
#  *
#  * Input: nums1 = [1, 2, 2], nums2 = [2, 1, 1]
#  * Output: false
#  *
#  * Input: nums1 = [4, 5, 6], nums2 = [4, 6, 5]
#  * Output: true
#  *
#  * Constraints:
#  * - 1 <= nums1.length, nums2.length <= 10^4
#  * - -10^6 <= nums1[i], nums2[i] <= 10^6
#  */

# define a function findPermutations() passing 2 parameters nums1, nums2
# def findPermutations(nums1, nums2):
#    use an if statement to check if the the length of nums1 and nums2 are not the same
#    if len(nums1) != len(nums2):
#        return false
#    use a for in loop to iterate on nums1
#    for num in nums1:
#        use an if statement to check if num is not in nums2
#        if num not in nums2:
#            return False
# return True       


def findPermutations(nums1, nums2):
    if len(nums1) != len(nums2):
        return False
    for num in nums1:
        if num not in nums2:
            return False
        nums2.remove(num)
    return True

print(findPermutations([1, 1, 2], [2, 2, 1]))