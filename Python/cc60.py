# /**
#  * LeetCode-style Problem (Easy-Medium): Check for Unique Elements in an Array
#  *
#  * Given an integer array `nums`, determine whether all elements in the array are unique.
#  * Return `true` if no element appears more than once; otherwise, return `false`.
#  *
#  * Your task is to write a function that checks for duplicate elements in the array.
#  *
#  * Parameters:
#  * - int[] nums: a non-empty array of integers
#  *
#  * Returns:
#  * - boolean: `true` if all elements are unique, `false` if there are duplicates
#  *
#  * Examples:
#  * Input: nums = [1, 2, 3, 4]
#  * Output: true
#  *
#  * Input: nums = [1, 2, 2, 3]
#  * Output: false
#  *
#  * Input: nums = [10]
#  * Output: true
#  *
#  * Constraints:
#  * - 1 <= nums.length <= 10^5
#  * - -10^9 <= nums[i] <= 10^9
#  */


# define a function findDuplicates() passing nums
#  def findDuplicates(nums):
#       create an empty list uniqueNums
#       uniqueNums = []
#       use a for in loop to iterate on nums
#       for num in nums:
#            use an if statement to check the condition uniqueNums.inclcudes(num)
#            if num in uniqueNums:
#               return false
# 
#            uniqueNums.add(num)     
#      return true


def findDuplicates(nums):
    uniqueNums = []
    for num in nums:
        if num in uniqueNums:
            return False
        uniqueNums.append(num)     
    return True


print(findDuplicates([ 2, 3, 4, 1]))