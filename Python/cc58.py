
# LeetCode-style Problem (Easy-Medium): Find Non-Common Elements Between Two Arrays
#
# Given two integer arrays nums1 and nums2, return a new array containing all the unique
# numbers that appear in only one of the two arrays (i.e., not shared between them).
# The result should not contain duplicates, and the order of elements does not matter.
#
# Parameters:
# - int[] nums1: A non-empty array of integers
# - int[] nums2: A non-empty array of integers
#
# Returns:
# - int[]: An array of integers that are unique to either nums1 or nums2 (but not both)
#
# Examples:
# Input: nums1 = [1, 2, 3], nums2 = [2, 3, 4]  
# Output: [1, 4]
#
# Input: nums1 = [5, 6, 7], nums2 = [7, 8, 9]  
# Output: [5, 6, 8, 9]
#
# Input: nums1 = [1, 1, 2], nums2 = [2, 3]  
# Output: [1, 3]
#
# Constraints:
# - 1 <= nums1.length, nums2.length <= 10^4
# - -10^6 <= nums1[i], nums2[i] <= 10^6

# define a function findsUniqueNums passing in 2 parameters nums1 and nums2
# def findsUniqueNums(nums1, nums2):
#       declare a variable uniqueNums and set equal to an empty set()
#       uniqueNums = set()
#       use a for in loop to iterate on nums1
#       for num in nums1:
#           use an if statement to check for the condition num not in nums2: 
#           if num not in nums2:
#               when true use .add() and passing in num to populate uniqueNums
#               uniqueNums.add(num)
#       use a second for in loop to iterate on nums2
#       for num in nums2:
#           use an if statement to check for the condition num not in nums1: 
#           if num not in nums1:
#               when true use .add() and passing in num to populate uniqueNums
#               uniqueNums.add(num)
#       return list(uniqueNums)


def findsUniqueNums(nums1, nums2):
    uniqueNums = set()
    for num in nums1:
        if num not in nums2:
            uniqueNums.add(num)
    for num in nums2:
        if num not in nums1:
            uniqueNums.add(num)
    return list(uniqueNums)

def findsUniqueNums2(nums1, nums2):
    uniqueNums = set()
    for num in nums1 + nums2:
        if not (num in nums1 and num in nums2):
            uniqueNums.add(num)
    return list(uniqueNums)


print(findsUniqueNums([1, 2, 3], [2, 3, 4]))