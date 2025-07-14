# LeetCode-style Problem: Square Each Number
#
# Given an array of integers `nums`, return a new array where each element
# is the square of the corresponding element in the input array.
#
# Parameters:
# int[] nums - a non-empty array of integers
#
# Returns:
# int[] - an array containing the squares of the input numbers
#
# Examples:
# Input: nums = [1, 2, 3, 4]
# Output: [1, 4, 9, 16]
#
# Input: nums = [-1, -2, -3]
# Output: [1, 4, 9]
#
# Input: nums = [0]
# Output: [0]
#
# Constraints:
# - 1 <= nums.length <= 10^4
# - -10^3 <= nums[i] <= 10^3
#/

# define a function called squareNums passing 1 parameter nums
# def squareNums(nums):
#      declare a variable a variable called squaredR let type and set to []   
#      squaredR = []
#      use a for loop to iterate on nums using num
#      for num in nums:
#          set squaredR to [num ** 2]
#          squaredR.append(num ** 2)
#      }
#      return squaredR
#}

def squareNums(nums):
    squaredR = []
    for num in nums:
        squaredR.append(num ** 2) 
    return squaredR


print(squareNums([1, 2, 3, 4]))