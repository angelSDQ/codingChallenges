/**
 * LeetCode-style Problem (Easy): Check if All Elements Are the Same
 *
 * Given an integer array `nums`, determine whether **all elements in the array are the same**.
 * Return `true` if every element is equal to the first one; otherwise, return `false`.
 *
 * Parameters:
 * - int[] nums: a non-empty array of integers
 *
 * Returns:
 * - boolean: true if all elements in the array are equal, false otherwise
 *
 * Examples:
 * Input: nums = [2, 2, 2, 2]
 * Output: true
 *
 * Input: nums = [1, 2, 1]
 * Output: false
 *
 * Input: nums = [7]
 * Output: true
 *
 * Constraints:
 * - 1 <= nums.length <= 10^5
 * - -10^9 <= nums[i] <= 10^9
 */

// create a class cc24
// create a the main method inside the class
// public static void main(String[] args) {
//      int[] nums = {};
//      System.out.println(findDuplicates(nums));
//}
//create a method findAllDuplicates() of boolean type passing 1 parameter int[] nums
//public static boolean findAllDuplicates(int[] nums) {
//      declare a List for duplicateNums with the inital value of nums[0]
//      List<Integer> duplicateNums = new ArrayList<>(Arrays.asList(nums[0]));
//      use a for loop to iterate on nums starting at index 1
//      for (int i = 1; i < nums.length; i++) {
//          use an if statement to check for the condition !(duplicateNums.contains(nums[i]
//          if (!(duplicateNums.contains(nums[i]))) {
//              return false;
//          }
//          duplicateNums.add(num);     
//      }
//      return true;
//  }

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class cc24 {
    public static void main(String[] args) {
        int[] nums = {2, 3, 2, 2};
        System.out.println(findAllDuplicates(nums));
}
    public static boolean findAllDuplicates(int[] nums) {
        List<Integer> duplicateNums = new ArrayList<>(Arrays.asList(nums[0]));
        for (int i = 1; i < nums.length; i++) {
            if (!(duplicateNums.contains(nums[i]))) {
                return false;
            }
            duplicateNums.add(nums[i]);     
        }
        return true;
    }
}
