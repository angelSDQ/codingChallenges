
#  * LeetCode-style Problem: Filter Even Numbers from Array
#  *
#  * Given an array of integers `nums`, return a new array containing only the
#  * even numbers
#  * from the original array, in the same order.
#  *
#  * Parameters:
#  * int[] nums - a non-empty array of integers
#  *
#  * Returns:
#  * int[] - an array of even integers from the input array
#  *
#  * Examples:
#  * Input: nums = [1, 2, 3, 4, 5, 6]
#  * Output: [2, 4, 6]
#  *
#  * Input: nums = [11, 13, 15]
#  * Output: []
#  *
#  * Input: nums = [0, -2, -3, 8]
#  * Output: [0, -2, 8] 


# define a function gettingEven passing 1 parameter nums
# def gettingEven(nums):
#       declare a variable allEvenNums and set to []
#       allEvenNums = []
#       use a for loop to iterate on nums using range len 
#       for i in range(len(nums)):
#           use an if statement to check for the condition nums[i] % 2 == 0
#           if nums[i] % 2 == 0:
#               populate allEvenNums using .append and pass nums[i] to add each one
#               allEvenNums.append(nums[i])
#       return allEvenNums

def gettingEven(nums):
    allEvenNums = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            allEvenNums.append(nums[i])
    return allEvenNums

print(gettingEven([0, -2, -3, 8]))