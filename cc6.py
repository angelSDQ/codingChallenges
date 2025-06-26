# PROBLEM

# Given a list nums and an integer target, return the index of the first occurrence of target. If not found, return -1.
# Example 1:
# Input: nums = [1, 2, 3, 4], target = 3
# Output: 2
# Example 2:
# Input: nums = [1, 2, 3, 4], target = 5
# Output: -1
# Constraints:
# •	1 <= nums.length <= 10⁵
# •	-10⁹ <= nums[i], target <= 10⁹

# SOLUTION

# Declare a function indexPosition() pass => nums (the list of numbers) and target 
# def indexPosition(nums, target):
#   Use for loop to iterate through the indices of nums
#   for index in range(len(nums)): # range starts at 0 and len goes from begin to end of the list => nums[index] (element)
#       use an if statement 
#       if nums[index] == target:
#           return index
# return -1 outside the for loop after all of the iterations inside the for loops are finished
#   return -1
#
# print and call indexPosition(nums, target)

# PROBLEM

def indexPosition(nums, target): 
    for index in range(len(nums)):
        if nums[index] == target:
            return index
    return -1

print(indexPosition([1, 2, 3, 4], 3))