/*
 * LeetCode-style Problem: Raise Numbers to a Power
 *
 * Given an array of integers `nums` and an integer `exponent`, return a new array
 * where each element is raised to the power of `exponent`.
 *
 * Parameters:
 * int[] nums - a non-empty array of integers
 * int exponent - a non-negative integer representing the power to raise each number to
 *
 * Returns:
 * int[] - an array containing each number in `nums` raised to the power of `exponent`
 *
 * Examples:
 * Input: nums = [2, 3, 4], exponent = 2
 * Output: [4, 9, 16]
 *
 * Input: nums = [1, -1, 2], exponent = 3
 * Output: [1, -1, 8]
 *
 * Input: nums = [5], exponent = 0
 * Output: [1]
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^3 <= nums[i] <= 10^3
 * - 0 <= exponent <= 10
 */

// import ArrayList and List
// import java.util.ArrayList;
// import java.util.List;

// create a class 
// create main method inside the class
// public static void main(String[] args){
//        int[] nums = {2, 3, 4};
//        int exponent = 2;
//        int[] raisedN = raisedToExponent(nums, exponent);
//        for (int i = 0; i < raisedN.length; i++) {
//              System.out.println(raisedN[i]);
//        }
// }
// declare a method called raisedToExponent() of int[] type passing 2 parameters of int[] type nums and exponent
// public static int[] raisedToExponent(int[]nums, int exponent){
//      declare an array list for plainNums
//      List<Integer> nums&Exponent = new ArrayList<>();
//      use a for loop to iterate on nums
//      for (int i = 0; i < nums; i++) {
//      nums&Exponent.add(nums * exponent);
//}
//      int[] raisedNum = new int[numsExponent.size()]
//      for (int i = 0; i < numsExponent.size(); i++) {
//              use raisedNum[i] and set to numsExponent.get(i) to start populating raisedNum get() retrieves the element from the ArrayList
//              raisedNum[i] = numsExponent.get(i);
//      return raisedNum;

import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

public class cc13 {
    public static void main(String[] args){
        int[] nums = {1, -1, 2};
        int exponent = 3;
        int[] raisedN = raisedToExponent(nums, exponent);
        for (int i = 0; i < raisedN.length; i++) {
            System.out.println(raisedN[i]);
        }
    }
    public static int[] raisedToExponent(int[]nums, int exponent){
        List<Integer> numsExponent = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            numsExponent.add((int) Math.pow(nums[i], exponent));
        }
        int[] raisedNum = new int[numsExponent.size()];
        for (int i = 0; i < numsExponent.size(); i++) {
            raisedNum[i] = numsExponent.get(i);
        }
    return raisedNum;
    }
}