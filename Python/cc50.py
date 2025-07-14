# LeetCode-style Problem: Raise Numbers to a Power
#
# Given an array of integers `nums` and an integer `exponent`, return a new array
# where each element is raised to the power of `exponent`.
#
# Parameters:
# int[] nums - a non-empty array of integers
# int exponent - a non-negative integer representing the power to raise each number to
#
# Returns:
# int[] - an array containing each number in `nums` raised to the power of `exponent`
#
# Examples:
# Input: nums = [2, 3, 4], exponent = 2
# Output: [4, 9, 16]
#
# Input: nums = [1, -1, 2], exponent = 3
# Output: [1, -1, 8]
#
# Input: nums = [5], exponent = 0
# Output: [1]
#
# Constraints:
# - 1 <= nums.length <= 10^4
# - -10^3 <= nums[i] <= 10^3
# - 0 <= exponent <= 10
#/



# define a function called raisedToExponent passing 2 parameters of int[] type nums and exponent
# def raisedToExponent(nums, exponent):
#       create a variable squaredNums and set to []
#       squaredNums = []; 
#       use a for loop to iterate on nums
#       for num in nums:
#           use .append() and pass num ** exponent 
#           squaredNums.append(num ** exponent)
#       return squaredNums


def raisedToExponent(nums, exponent):
    squaredNums = []; 
    for num in nums:
        squaredNums.append(num ** exponent)
    return squaredNums
print(raisedToExponent([1, -1, 2], 3))