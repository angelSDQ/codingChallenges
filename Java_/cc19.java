/**
 * LeetCode-style Problem (Easy): Check if Target Exists in Array
 *
 * Given an array of integers `nums` and an integer `target`, return true if the target
 * exists in the array, and false otherwise.
 *
 * Parameters:
 * - int[] nums: A non-empty array of integers
 * - int target: The integer to search for
 *
 * Returns:
 * - boolean: true if target exists in nums, false otherwise
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4, 5], target = 3  
 * Output: true
 *
 * Input: nums = [10, 20, 30], target = 25  
 * Output: false
 *
 * Input: nums = [-5, -2, 0, 2, 5], target = -2  
 * Output: true
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^6 <= nums[i], target <= 10^6
 */


// create a class cc19
//      inside the class declare a main method 
//      public static void main(String[] args) {
//          declare variables
//          int[] nums = [];
//          int target = 0
//          System.out.println(findingTargetNum(nums, target));
//      }
//      create a method findingTargetNum() of boolean type passing in 2 parameters (int[] nums, int target)
//      public static boolean findingTargetNum(int[] nums, int target) {
//          use a for each loop to iterate on nums
//          for (int num : nums) {
//              use an if statement to check for the condition (num == target)
//              if (num == target) {
//                  return true;
//              } else {
//                  return false;
//              }
//          }
//      }

import java.util.Arrays;

public class cc19 {
        public static void main(String[] args) {
            int[] nums = {1, 2, 3, 41, 5};
            int target = 41;
            System.out.println(findingTargetNum(nums, target));
    }
    public static boolean findingTargetNum(int[] nums, int target) {
        if (Arrays.binarySearch(nums, target) >= 0) {
            return true;
        } 
        return false;
    }
}
