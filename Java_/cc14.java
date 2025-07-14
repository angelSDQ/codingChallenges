/*
 * LeetCode-style Problem: Double Odd Numbers
 *
 * Given an array of integers `nums`, return a new array where each odd number
 * is doubled and each even number remains the same.
 *
 * Parameters:
 * int[] nums - a non-empty array of integers
 *
 * Returns:
 * int[] - an array where odd numbers are doubled, and even numbers stay unchanged
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4]
 * Output: [2, 2, 6, 4]
 *
 * Input: nums = [0, -1, -2, 5]
 * Output: [0, -2, -2, 10]
 *
 * Input: nums = [8, 7, 6]
 * Output: [8, 14, 6]
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^6 <= nums[i] <= 10^6
 */

// import ArrayList, List, Math
// import java.util.ArrayList;
// import java.util.List;
// import java.lang.Math;

//create a class
//declare a main method inside the class
//public static void main(String[] args) {
//  create a variable of int[] type called nums set to {}
//  int[] nums = {};
//  create a variable returnsDoubleOdds set to doublingEvens(nums)
//  int[] returnsDoubleOdds = doublingEvens(nums);
//  use a for loop to iterate on returnsDoubleOdds using .length
//  for (int i = 0; i < returnsDoubleOdds.length; i++) {
//      print returnsDoubleOdds[i]
//      System.out.println(returnsDoubleOdds[i]);
//}
//declare a method named doublingEvens() of int[] type and passing in one parameter int[] nums
//public static int[] doublingEvens(int[] nums) {}
//      declare an array list for modifiedNums
//      List<Integer> modifiedNums = new ArrayList<>();
//      use a for loop to iterate on nums(parameter) using .length to get all numbers
//      for (int i = 0; i < nums.length; i++) {
//          use an if statement to check the condition nums[i] % 2 == 1 we want to divide the numbers by 2 if its an odd number
//          if (nums[i] % 2 == 1) {
//              when true the odd number will be doubled or multiplied by 2 use Math.pow(nums[i] * 2)
//              modifiedNums.add((int) Math.pow(nums[i] * 2));
//          }
//      }
//      initialize new variable set to new int[modifiedNums.size()] this will be use for the return
//      int[] doubledOddNums = new int[modifiedNums.size()]
//      for (int i = 0; i < modifiedNums.size(); i++) {
//              use doubledOddNums[i] and set to modifiedNums.get(i) to start populating raisedNum get() retrieves the element from the ArrayList
//              doubledOddNums[i] = modifiedNums.get(i);
//      return doubledOddNums;


public class cc14 {
    public static void main(String[] args) {
        int[] nums = {0, -1, -2, 5};
        int[] returnsDoubleOdds = doublingEvens(nums);
        for (int num : returnsDoubleOdds) {
            System.out.println(num);
        }
    }
    public static int[] doublingEvens(int[] nums) {
        int[] doubledOddNums = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 1 || nums[i] % 2 == -1) {
                doubledOddNums[i] = nums[i] * 2;
            } else {
                doubledOddNums[i] = nums[i];
            }
        }
    return doubledOddNums;
    }
}
