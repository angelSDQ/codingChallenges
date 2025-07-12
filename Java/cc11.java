package Java;
/**
 * LeetCode-style Problem: Filter Even Numbers from Array
 *
 * Given an array of integers `nums`, return a new array containing only the
 * even numbers
 * from the original array, in the same order.
 *
 * Parameters:
 * int[] nums - a non-empty array of integers
 *
 * Returns:
 * int[] - an array of even integers from the input array
 *
 * Examples:
 * Input: nums = [1, 2, 3, 4, 5, 6]
 * Output: [2, 4, 6]
 *
 * Input: nums = [11, 13, 15]
 * Output: []
 *
 * Input: nums = [0, -2, -3, 8]
 * Output: [0, -2, 8] 
*/

// create a class cc11 
//      create a main method inside the class
//      public static void main(String[] args) {
//      create a new variable of int[] type for the parameter
//      int[] nums = {};
//      int[] evenNumbers = gettingEven(nums);
//      use a for loop to iterate and then print result
//      for (int i = 0; i < evenNumbers.length; i++) {
//          System.out.println(evenNumbers[i]);
//}
//      create a method called gettingEven of int[] type passing 1 parameter nums of int[] type
//      public static int[] gettingEven(int[] nums) {
//          declare an array list for allEvenNums
//          List<Integer> allEvenNums = new ArrayList<>();
//          use a for loop to iterate on nums(parameter) using .length to get all numbers
//          for (int i = 0; i < nums.length; i++) {
//              use an if statement to check the condition nums[i] % 2 == 0 we want to divide the numbers by 2 if its even and nothing remains we have an even number
//              if (nums[i] % 2 == 0) {
//                  use .add passing the nums[i] to add all the numbers to allEvensHere
//                  allEvenNums.add(nums[i])
//}
//          int[] putEvensHere = new int[allEvenNums.size()]
//          for (int i = 0; i < allEvenNums.size(); i++) {
//              use putEvensHere[i] and set to allEvenNums.get(i) to start populating putEvensHere get() retrieves the element from the ArrayList
//              putEvensHere[i] = allEvenNums.get(i);
//          return putEvensHere
//}
//}
//}
import java.util.ArrayList;
import java.util.List;
public class cc11 {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 6};
        int[] evenNumbers = gettingEven(nums);
        for (int i = 0; i < evenNumbers.length; i++) {
            System.out.println(evenNumbers[i]);
        }
    }
    public static int[] gettingEven(int[] nums) {
        List<Integer> allEvenNums = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                allEvenNums.add(nums[i]);
            }
        }
        int[] putEvensHere = new int[allEvenNums.size()];
        for (int i = 0; i < allEvenNums.size(); i++) {
            putEvensHere[i] = allEvenNums.get(i);
        }
    return putEvensHere;
    }


}
