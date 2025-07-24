# LeetCode-style Problem (Easy): Check if All Elements Are the Same
#
# Given an integer array `nums`, determine whether##all elements in the array are the same##.
# Return `true` if every element is equal to the first one; otherwise, return `false`.
#
# Parameters:
# - int[] nums: a non-empty array of integers
#
# Returns:
# - boolean: true if all elements in the array are equal, false otherwise
#
# Examples:
# Input: nums = [2, 2, 2, 2]
# Output: true
#
# Input: nums = [1, 2, 1]
# Output: false
#
# Input: nums = [7]
# Output: true
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9

#define a function findAllDuplicates passing in 1 parameter nums
#def findAllDuplicates(nums):
#   create a list duplicateNums set to []
#   duplicateNums = []
#   use a in loop to iterate on nums
#   for num in nums:
#       use an if statement to check for the condition num not in duplicateNums
#       if num not in duplicateNums:
#           return False;
#       duplicateNums.append(num)     
#   return True


def findAllDuplicates(nums):
    duplicateNums = [nums[0]]
    for i in range(1, len(nums)):
        if (nums[i] not in duplicateNums):
            return False
        duplicateNums.append(nums[i])     
    return True

print(findAllDuplicates([2, 2, 2]))
