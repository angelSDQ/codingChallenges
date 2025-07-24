/**
 * LeetCode-style Problem (Easy-Medium): Check for Unique Elements in an Array
 *
 * Given an integer array `nums`, determine whether all elements in the array are unique.
 * Return `true` if no element appears more than once; otherwise, return `false`.
 *
 * Your task is to write a function that checks for duplicate elements in the array.
 *
 * Parameters:
 * - int[] nums: a non-empty array of integers
 *
 * Returns:
 * - boolean: `true` if all elements are unique, `false` if there are duplicates
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4]
 * Output: true
 *
 * Input: nums = [1, 2, 2, 3]
 * Output: false
 *
 * Input: nums = [10]
 * Output: true
 *
 * Constraints:
 * - 1 <= nums.length <= 10^5
 * - -10^9 <= nums[i] <= 10^9
 */

// IMPORT
// import java.util.ArrayList;
// import java.util.List;

// create a class cc23
//  inside the class declare the main method
//  public static void main(String[] args) {
//      int[] nums = {};
//      System.out.println(findDuplicates(nums));

//  }
//  create a method findDuplicates() of boolean type and pass 1 parameter int[] nums
//  public static boolean findDuplicates(int[] nums) {
//      declare a Hashset for numsToKeep
//      List<Integer> uniqueNums = new ArrayList<>();
//      use a for each loop to iterate on nums
//      for (int num : nums) {
//          use an if statement to check for the condition
//          if (uniqueNums.contains(num)) {
//              return false;
//          }
//          uniqueNums.add(num);     
//      }
//      return true;
//  }

import java.util.ArrayList;
import java.util.List;

public class cc23 {
        public static void main(String[] args) {
        int[] nums = {1, 2, 4, 4, 5};
        System.out.println(findDuplicates(nums));

    }
    public static boolean findDuplicates(int[] nums) {
        List<Integer> uniqueNums = new ArrayList<>();
        for (int num : nums) {
            if (uniqueNums.contains(num)) {
                return false;
            }
            uniqueNums.add(num);     
        }
        return true;
    }
}
