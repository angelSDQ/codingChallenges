#
# •  LeetCode-style Problem (Easy-Medium): Filter Numbers Divisible by Two Given Values
#  *
# •  Given an array of integers nums and two integers a and b,
# •  return a new array containing only the numbers from nums that are divisible by both a and b,
# •  in the same order as they appear in the original array.
#  *
# •  Parameters:
# •  - int[] nums: A non-empty array of integers
# •  - int a: First positive integer divisor
# •  - int b: Second positive integer divisor
#  *
# •  Returns:
# •  - int[]: An array of integers from the input array that are divisible by both a and b
#  *
# •  Examples:
# •  Input: nums = [4, 6, 8, 12, 18], a = 2, b = 3  
# •  Output: [6, 12, 18]  // 6, 12, and 18 are divisible by both 2 and 3
#  *
# •  Input: nums = [10, 15, 20, 30, 45], a = 5, b = 10  
# •  Output: [10, 20, 30]  // divisible by both 5 and 10
#  *
# •  Input: nums = [1, 2, 3, 4, 5], a = 7, b = 8  
# •  Output: []  // no numbers are divisible by both 7 and 8
#  *
# •  Constraints:
# •  - 1 <= nums.length <= 10^4
# •  - -10^6 <= nums[i] <= 10^6
# •  - 1 <= a, b <= 1000
#

# define a funtion numbersDivisibleByAandB() passing 3 parameters (nums, a, b)
# def numbersDivisibleByAandB(nums, a, b):
#   create a variable findingDivisibleNums set to []
#   findingDivisibleNums = []
#   use a for loop to iterate on findingDivisibleNums
#   for num in nums:
#       use an if statement to check for the condition --> num % a == 0 and num % b == 0
#       if num % a == 0 and num % b == 0:
#           when true, to populate findingDivisibleNums use .append passing in num
#           findingDivisibleNums.append(num)
#   return findingDivisibleNums

def numbersDivisibleByAandB(nums, a, b):
    findingDivisibleNums = []
    for num in nums:
        if num % a == 0 and num % b == 0:
            findingDivisibleNums.append(num)
    return findingDivisibleNums

print(numbersDivisibleByAandB([1, 2, 3, 4, 5], 7, 8))