# /**
#  * LeetCode-style Problem: Reverse a List
#  *
#  * Given a list of integers `nums`, return the list in reversed order.
#  *
#  * Examples:
#  * Input: nums = [1, 2, 3]
#  * Output: [3, 2, 1]
#  *
#  * Input: nums = [5]
#  * Output: [5]
#  * Input: nums = [4, 8, 15, 16, 23, 42]
#  * Output: [42, 23, 16, 15, 8, 4]
#  *
#  * Input: nums = [10, -1, 0, 7]
#  * Output: [7, 0, -1, 10]
#  *
#  * Constraints:
#  * - 1 <= nums.length <= 10^5
#  * - -10^9 <= nums[i] <= 10^9
#  * 
#  */

# define a function reversingNums() pssing one parameter nums
# def reversingNums(nums):
    # create a variable numsReversed set to empty []
    # numsReversed = []
    # use a for loop to iterate on nums using range len to do it backwards 
    # for i in range(len(nums)-1, -1, -1):
        # use .append() pass nums[i] to populate numsReversed with the elements from nums
        # numsReversed.append(nums[i])
# return numsReversed

def reversingNums(nums):
    numsReversed = []
    for i in range(len(nums)-1, -1, -1):
        numsReversed.append(nums[i])
    return numsReversed

print(reversingNums([4, 8, 15, 16, 23, 42]))

