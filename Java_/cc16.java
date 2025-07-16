package Java_;
/**
 * LeetCode-style Problem (Easy-Medium): Filter Numbers Outside a Range
 *
 * Given an array of integers nums, and two integers low and high,
 * return a new array containing only the numbers that are *strictly outside the range (low, high)*,
 * in the same order as they appear in the original array.
 *
 * Parameters:
 * - int[] nums: A non-empty array of integers
 * - int low: The lower bound of the range (exclusive)
 * - int high: The upper bound of the range (exclusive)
 *
 * Returns:
 * - int[]: An array of integers from the input array that lie outside the exclusive range (low, high)
 *
 * Examples:
 * Input: nums = [1, 5, 10, 15, 20], low = 5, high = 15  
 * Output: [1, 20]
 *
 * Input: nums = [-10, -5, 0, 5, 10], low = -5, high = 5  
 * Output: [-10, 10]
 *
 * Input: nums = [100, 200, 300], low = 0, high = 500  
 * Output: []
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^6 <= nums[i], low, high <= 10^6
 * - low < high
 */

// IMPORT
// import java.util.ArrayList;
// import java.util.List;

//create a class
//      create a main method inside the class
//      public static void main(String[] args) {
//          int[] nums = {-10, -5, 0, 5, 10};
//          int low = -5;
//          int high = 5;
//          int[] outRangeNums = findingExcludedRange(nums, low, high);
//          for (int num : outRangeNums) {
//              System.out.println(num);
//          }
//      }
//      create a method findingExcludedRange() of int[] type passing 3 parameters int[] nums, int low, int high
//      public static int[] findingExcludedRange(int[] nums, int low, int high) {
//      declare an array list for excludedRange
//      List<Integer> excludedRange = new ArrayList<>();
//      use a for loop to iterate on nums use (num : nums)
//      for (num : nums) {
//          use an if statement to check the condition (num < low && num > high)
//          if (int num < low && num > high) {
//              if true use .add() to populate excludedRange
//              excludedRange.add(num);
//          }
//      instantiate numsOutOfRange set to new int[] passing excludedRange using .size()
//      int[] numsOutOfRange = new int[excludedRange.size()];
//      use a for loop to iterate on excludedRange.size()
//      for (int i = 0; i < excludedRange.size(); i++) {
//           populate numsOutOfRange[i] set to excludedRange.get(i)
//           numsOutOfRange[i] = excludedRange.get(i);
//      }
//      return numsOutOfRange;
//      }
//}
//}

import java.util.ArrayList;
import java.util.List;

public class cc16 {
    public static void main(String[] args) {
        int[] nums = {1, 5, 10, 15, 20};
        int low = 5;
        int high = 15;
        int[] outRangeNums = findingExcludedRange(nums, low, high);
        for (int num : outRangeNums) {
            System.out.println(num);
        }
    }
    public static int[] findingExcludedRange(int[] nums, int low, int high) {
        List<Integer> excludedRange = new ArrayList<>();
        for (int num : nums) {
            if (num < low || num > high) {
                excludedRange.add(num);
            }
        }
        int[] numsOutOfRange = new int[excludedRange.size()];
        for (int i = 0; i < excludedRange.size(); i++) {
            numsOutOfRange[i] = excludedRange.get(i);
        }
    return numsOutOfRange;
    }
}
