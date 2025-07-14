#
# LeetCode-style Problem: Double Odd Numbers
#
# Given an array of integers `nums`, return a new array where each odd number
# is doubled and each even number remains the same.
#
# Parameters:
# int[] nums - a non-empty array of integers
#
# Returns:
# int[] - an array where odd numbers are doubled, and even numbers stay unchanged
#
# Examples:
# Input: nums = [1, 2, 3, 4]
# Output: [2, 2, 6, 4]
#
# Input: nums = [0, -1, -2, 5]
# Output: [0, -2, -2, 10]
#
# Input: nums = [8, 7, 6]
# Output: [8, 14, 6]
#
# Constraints:
# - 1 <= nums.length <= 10^4
# - -10^6 <= nums[i] <= 10^6
#/

# define a function doublingEvens() passing in one parameter nums
#def doublingEvens(nums):
#   create a variable modifiedNums set to []
#   modifiedNums = []
#   use a for loop to iterate on nums(parameter)
#   for num in nums:
    #   use an if statement to check the condition num % 2 == 1 or num % 2 == -1 we want to divide the numbers by 2 if its an odd number
    #   if (nums[i] % 2 == 1 or num % 2 == -1):
    #   when true the odd number will be doubled or multiplied by 2 use .append to add the elements to modifiedNums
    #       modifiedNums.append(num * 2)
    #   else:
    #       modifiedNums.append(num)
# return modifiedNums

def doublingEvens(nums):
    modifiedNums = []
    for num in nums:
        if num % 2 == 1 or num % 2 == -1:
            modifiedNums.append(num * 2)
        else:
            modifiedNums.append(num)
    return modifiedNums

print(doublingEvens([1, 2, 3, 4]))