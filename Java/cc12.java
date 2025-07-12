package Java;
/*
 * LeetCode-style Problem: Square Each Number
 *
 * Given an array of integers `nums`, return a new array where each element
 * is the square of the corresponding element in the input array.
 *
 * Parameters:
 * int[] nums - a non-empty array of integers
 *
 * Returns:
 * int[] - an array containing the squares of the input numbers
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4]
 * Output: [1, 4, 9, 16]
 *
 * Input: nums = [-1, -2, -3]
 * Output: [1, 4, 9]
 *
 * Input: nums = [0]
 * Output: [0]
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^3 <= nums[i] <= 10^3
 */

// import list and arraylist
// create a class
// create the main method inside the class
// public static void main(String[] args) {}
//      create a new variable of int[] type for the parameter
//      int[] nums = {};
//      int[] squareAnswer = squareNums(nums);
//      use a for loop to iterate and then print result
//      for (int i = 0; i < squareAnswer.length; i++) {
//          System.out.println(squareAnswer[i]);
//}
// create a method squareNums() of int[] type passing in 1 parameter nums of int[]
// public static int[] squareNums(int[] nums) {
//      declare an array list for squaringSolution
//      List<Integer> squaringSolution = new ArrayList<>();
//      use a for loop to iterate on nums(parameter) using .length to get all numbers
//      for (int i = 0; i < nums.length; i++) {
//          to get the square of the corresponding number multiply it times itself
//          squaringSolution.add(nums[i] * nums[i]);
//      }
//      int[] finalSolution = new int[squaringSolution.size()]
//      for (int i = 0; i < squaringSolution.size(); i++) {
//              use solutionHere[i] and set to squaringSolution.get(i) to start populating solutionHere get() retrieves the element from the ArrayList
//              solutionHere[i] = squaringSolution.get(i);
//      return solutionHere

import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

public class cc12 {
    public static void main(String[] args) {
        int[] nums = {-1, -2, -3};
        int[] squareAnswer = squareNums(nums);
        for (int i = 0; i < squareAnswer.length; i++) {
            System.out.println(squareAnswer[i]);
        }
    }
    public static int[] squareNums(int[] nums) {
        List<Integer> squaringSolution = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            squaringSolution.add((int) Math.pow(nums[i], 2));
            //squaringSolution[i] = ;
        }
    
        int[] finalSolution = new int[squaringSolution.size()];
        for (int i = 0; i < squaringSolution.size(); i++) {
            finalSolution[i] = squaringSolution.get(i);
        }
    return finalSolution;
    }
}