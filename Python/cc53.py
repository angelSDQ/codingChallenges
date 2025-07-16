#
# LeetCode-style Problem (Easy-Medium): Filter Numbers Outside a Range
#
# Given an array of integers nums, and two integers low and high,
# return a new array containing only the numbers that are#strictly outside the range (low, high)*,
# in the same order as they appear in the original array.
#
# Parameters:
# - int[] nums: A non-empty array of integers
# - int low: The lower bound of the range (exclusive)
# - int high: The upper bound of the range (exclusive)
#
# Returns:
# - int[]: An array of integers from the input array that lie outside the exclusive range (low, high)
#
# Examples:
# Input: nums = [1, 5, 10, 15, 20], low = 5, high = 15  
# Output: [1, 20]
#
# Input: nums = [-10, -5, 0, 5, 10], low = -5, high = 5  
# Output: [-10, 10]
#
# Input: nums = [100, 200, 300], low = 0, high = 500  
# Output: []
#
# Constraints:
# - 1 <= nums.length <= 10^4
# - -10^6 <= nums[i], low, high <= 10^6
# - low < high


# define a function numsNotInRange() passing in 3 parameters nums, low, high (these last two are inclusive)
# def numsNotInRange(nums, low, high)
#       create a variable numsOutOfRange set to []
#       numsOutOfRange = []
#       use a for loop to iterate on nums 
#       for num in nums:
#           use an if statement to check for the condition (num < low or num > high)
#           if (num < low or num > high):
#               populate numsOutOfRange using .append() passing in num
#               numsOutOfRange.append(num)
#       return numsOutOfRange


def numsNotInRange(nums, low, high):
    numsOutOfRange = []
    for num in nums:
        if (num < low or num > high):
            numsOutOfRange.append(num)
    return numsOutOfRange

print(numsNotInRange([1, 5, 10, 15, 20], 5, 15))