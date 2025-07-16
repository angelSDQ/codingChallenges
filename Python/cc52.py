# /**
# •  LeetCode-style Problem (Easy-Medium): Filter Numbers Within a Range
#  *
# •  Given an array of integers nums, and two integers low and high, 
# •  return a new array containing only the numbers that are *within the range [low, high]*, inclusive,
# •  in the same order as they appear in the original array.
#  *
# •  Parameters:
# •  - int[] nums: A non-empty array of integers
# •  - int low: The lower bound of the range (inclusive)
# •  - int high: The upper bound of the range (inclusive)
#  *
# •  Returns:
# •  - int[]: An array of integers from the input array that lie within the range [low, high]
#  *
# •  Examples:
# •  Input: nums = [1, 5, 10, 15, 20], low = 5, high = 15  
# •  Output: [5, 10, 15]
#  *
# •  Input: nums = [-10, -5, 0, 5, 10], low = -5, high = 5  
# •  Output: [-5, 0, 5]
#  *
# •  Input: nums = [100, 200, 300], low = 0, high = 99  
# •  Output: []
#  *
# •  Constraints:
# •  - 1 <= nums.length <= 10^4
# •  - -10^6 <= nums[i], low, high <= 10^6
# •  - low <= high
#  *
# •  Required imports:
# •  import java.util.ArrayList;
# •  import java.util.List;
#  */

# declare a function called findLowHighNums() passing in 3 parameters nums, low, high (these last two are inclusive)
# def findLowHighNums(nums, low, high):
#       create a variable numsInRange set to []
#       lowAndHigh = []; 
#       use a for loop to iterate on nums using range(len()) passing in nums
#       for i in range(len(nums)):
#           use an if statement to find the low and high numbers condition
#           if nums[i] >= low and nums[i] <= high:
#              lowAndHigh.append(nums[i]);
#       return lowAndHigh;

def findLowHighNums(nums, low, high):
    lowAndHigh = []; 
    for num in nums:
        if num >= low and num <= high:
            lowAndHigh.append(num)
    return lowAndHigh

print(findLowHighNums([-10, -5, 0, 5, 10], -5, 5))