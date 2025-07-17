/**
•  LeetCode-style Problem (Easy-Medium): Filter Numbers Divisible by Two Given Values
 *
•  Given an array of integers nums and two integers a and b,
•  return a new array containing only the numbers from nums that are divisible by both a and b,
•  in the same order as they appear in the original array.
 *
•  Parameters:
•  - int[] nums: A non-empty array of integers
•  - int a: First positive integer divisor
•  - int b: Second positive integer divisor
 *
•  Returns:
•  - int[]: An array of integers from the input array that are divisible by both a and b
 *
•  Examples:
•  Input: nums = [4, 6, 8, 12, 18], a = 2, b = 3  
•  Output: [6, 12, 18]  // 6, 12, and 18 are divisible by both 2 and 3
 *
•  Input: nums = [10, 15, 20, 30, 45], a = 5, b = 10  
•  Output: [10, 20, 30]  // divisible by both 5 and 10
 *
•  Input: nums = [1, 2, 3, 4, 5], a = 7, b = 8  
•  Output: []  // no numbers are divisible by both 7 and 8
 *
•  Constraints:
•  - 1 <= nums.length <= 10^4
•  - -10^6 <= nums[i] <= 10^6
•  - 1 <= a, b <= 1000
 */


// IMPORT
// import java.util.ArrayList;
// import java.util.List;

// create a class cc18
// create a main method inside the class
// public static void main(String[] args) {
//      create 4 variables 
//      int[] nums = [];
//      int a = 0;
//      int b = 0;
//      int[] divisibleNums = numbersDivisibleByAandB(nums, a, b);
//      use a for loop to iterate on divisibleNums
//      for (int num : divisibleNums) {
//          System.out.println(num);
//      }
// }
// create a method numbersDivisibleByAandB() of int[] type passing 3 parameters int[] nums, int a, and int b
// public static int[] numbersDivisibleByAandB(int[] nums, int a, int b) {
//      declare an array list for findingDivisibleNums
//      List<Integer> findingDivisibleNums = new ArrayList<>();
//      use a for loop to iterate on nums
//      for (int num : nums) {
//          use an if statement to check for the condition (num % a == 0 && num % b == 0)
//          if (num % a == 0 && num % b == 0) {
//              when true use .add() to populate findingDivisibleNums
//              findingDivisibleNums.add(num);
//          }
//      instantiate a variable divisibleNums int[] type and set to new int[findingDivisibleNums.size()];
//      int[] divisibleNums = new int[findingDivisibleNums.size()];
//      use a for loop to itarate on findingDivisibleNums.size()
//      for (int i = 0; i < findingDivisibleNums.size(); i++) {
//          set divisibleNums[i] to findingDivisibleNums.get(i);
//          divisibleNums[i] = findingDivisibleNums.get(i);
//      }   
// return divisibleNums 
// }



import java.util.ArrayList;
import java.util.List;

public class cc18 {
    public static void main(String[] args) {
        int[] nums = {10, 15, 20, 30, 45};
        int a = 5;
        int b = 10;
        int[] divisibleNums = numbersDivisibleByAandB(nums, a, b);
        for (int num : divisibleNums) {
            System.out.println(num);
        }
    }
    public static int[] numbersDivisibleByAandB(int[] nums, int a, int b) {
        List<Integer> findingDivisibleNums = new ArrayList<>();
        for (int num : nums) {
            if (num % a == 0 && num % b == 0) {
                findingDivisibleNums.add(num);
            }
        }
        int[] divisibleNums = new int[findingDivisibleNums.size()];
        for (int i = 0; i < findingDivisibleNums.size(); i++) {
            divisibleNums[i] = findingDivisibleNums.get(i);
        }   
    return divisibleNums; 
    }
}

