/**
•  LeetCode-style Problem (Easy-Medium): Filter Numbers Within a Range
 *
•  Given an array of integers nums, and two integers low and high, 
•  return a new array containing only the numbers that are *within the range [low, high]*, inclusive,
•  in the same order as they appear in the original array.
 *
•  Parameters:
•  - int[] nums: A non-empty array of integers
•  - int low: The lower bound of the range (inclusive)
•  - int high: The upper bound of the range (inclusive)
 *
•  Returns:
•  - int[]: An array of integers from the input array that lie within the range [low, high]
 *
•  Examples:
•  Input: nums = [1, 5, 10, 15, 20], low = 5, high = 15  
•  Output: [5, 10, 15]
 *
•  Input: nums = [-10, -5, 0, 5, 10], low = -5, high = 5  
•  Output: [-5, 0, 5]
 *
•  Input: nums = [100, 200, 300], low = 0, high = 99  
•  Output: []
 *
•  Constraints:
•  - 1 <= nums.length <= 10^4
•  - -10^6 <= nums[i], low, high <= 10^6
•  - low <= high
 *
•  Required imports:
•  import java.util.ArrayList;
•  import java.util.List;
 */

// IMPORT
// import java.util.ArrayList;
// import java.util.List;

//create a class
//create a main method
// public static void main(String[] args) {
//      create 3 variables
//      int[] nums = {};
//      int high = {};
//      int low = {};
//      create a new variable and to findLowHighNums(nums, low, high) passing the 3 parameters
//      int[] rangeNums = findLowHighNums(nums, low, high);
//      use a for loop to iterate on the list and print the results
//      for (int i = 0; i < rangeNums.length; i++) {
//          System.out.println(rangeNums[i]);
// }
//}
//  create a method called findLowHighNums() of int[] type passing in 3 parameters int[] nums, int low, int high (these last two are inclusive)
//  public static int[] findLowHighNums(int[] nums, int low, int high) {
//      declare an array list for findLowHighNums
//      List<Integer> lowAndHigh = new ArrayList<>();
//      use a for loop to iterate on nums using .length
//      for (int i = 0; i < nums.length; i++) {
//          use an if statement to find the low and high numbers condition
//          if (nums[i] >= low && nums[i] <= high) {
//              lowAndHigh.add(nums[i]);
//      instantiate a new variable numsInRnage to add the other numbers
//      int[] numsInRange = new int[lowAndHigh.size()];
//      use a for loop to iterate on lowAndHigh use .size() to get the whole list
//      for (int i = 0; i < lowAndHigh.size(); i++) {
//          numsInRange[i] = lowAndHigh.get(i);
//      }
    //return numsInRange;

import java.util.ArrayList;
import java.util.List;

public class cc15 {
    public static void main(String[] args) {
        int[] nums = {-10, -5, 0, 5, 10};
        int low = -5;
        int high = 5;
        int[] rangeNums = findLowHighNums(nums, low, high);
        for (int num : rangeNums) {
            System.out.println(num);
        }
    }
    public static int[] findLowHighNums(int[] nums, int low, int high) {
        List<Integer> lowAndHigh = new ArrayList<>();
        for (int num : nums) {
            if (num >= low && num <= high) {
                lowAndHigh.add(num);
            }
        }
        int[] numsInRange = new int[lowAndHigh.size()];
        for (int i = 0; i < lowAndHigh.size(); i++) {
            numsInRange[i] = lowAndHigh.get(i);
        }
    return numsInRange;
    }
}

