package Java_;

/**
 * LeetCode-style Problem (Easy-Medium): Filter Numbers Whose Squares Are Less Than a Given Value
 *
 * Given an array of integers `nums` and a single integer `limit`,
 * return a new array containing only the numbers from `nums` whose squares are strictly less than `limit`,
 * in the same order as they appear in the original array.
 *
 * Parameters:
 * - int[] nums: A non-empty array of integers
 * - int limit: A positive integer to compare against the square of each number
 *
 * Returns:
 * - int[]: An array of integers from the input array whose squares are < limit
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4, 5], limit = 10  
 * Output: [1, 2, 3]  // because 1^2=1, 2^2=4, 3^2=9 are all < 10
 *
 * Input: nums = [-5, -2, 0, 2, 5], limit = 25  
 * Output: [-2, 0, 2]  // because (-2)^2=4, 0^2=0, 2^2=4 are all < 25
 *
 * Input: nums = [10, 20, 30], limit = 50  
 * Output: [10]  // 10^2=100 is not < 50, so result is []
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^3 <= nums[i] <= 10^3
 * - 1 <= limit <= 10^6
 */

// IMPORT
// import java.util.ArrayList;
// import java.util.List;
// import java.lang.Math;

// create a class cc17
// create a main method inside the class
// public static void main(String[] args) {
//      int[] nums = {-10, -5, 0, 5, 10};
//      int limit = -5;
//      int[] onlyLimitedSquared = findSquareLimit(nums, limit);
//          for (int nums : onlyLimitedSquared) {
//              System.out.println(nums);
//}
// create a method findSquareLimit() of int[] type passing in 2 parameters int[] nums and int limit
// public static int[] findSquareLimit(int[] nums,int limit) {
//      declare an array list for findingSquare
//      List<Integer> squareLimit = new ArrayList<>();
//      use a for loop to iterate on nums(parameter) using .length to get all numbers
//      int [] squaredNums = [];
//      for (int i = 0; i < nums.length; i++) {
//          squaredNums.add((int) Math.pow(nums[i], 2));
//          use an if statement to check for the condition 
//          if (squaredNums < limit) {
//              squareLimit.add(squaredNums);
//          }
//      }
//      instantiate numsWithLimits set to new int[] passing squareLimit using .size()
//      int[] numsWithLimits = new int[squareLimit.size()];
//      use a for loop to iterate on squareLimit.size()
//      for (int i = 0; i < squareLimit.size(); i++) {
//           populate numsWithLimits[i] set to squareLimit.get(i)
//           numsWithLimits[i] = squareLimit.get(i);
//      }
// }

import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

public class cc17 {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        int limit = 10;
        int[] numsLessThanLimitArr = findNumSquaredLessThanLimit(nums, limit);
        for (int num : numsLessThanLimitArr) {
            System.out.println(num);
        }
    }
    public static int[] findNumSquaredLessThanLimit(int[] nums,int limit) {
        List<Integer> numsLessThanLimitList = new ArrayList<>();
        for (int num : nums) {
            int numSquared = (int) Math.pow(num, 2);
            if (numSquared < limit) {
                numsLessThanLimitList.add(num);
            }
        }
        int[] numsLessThanLimitArr = new int[numsLessThanLimitList.size()];
        for (int i = 0; i < numsLessThanLimitList.size(); i++) {
            numsLessThanLimitArr[i] = numsLessThanLimitList.get(i);
        }
    return numsLessThanLimitArr;
    }
}
