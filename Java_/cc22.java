/**
 * LeetCode-style Problem (Medium): Check if Two Arrays Are Permutations of Each Other
 *
 * Given two integer arrays `nums1` and `nums2`, determine whether one is a permutation of the other.
 * Two arrays are permutations of each other if they contain the same elements with the same frequencies,
 * regardless of order.
 *
 * Your task is to write a function that returns `true` if the arrays are permutations of each other,
 * and `false` otherwise.
 *
 * Parameters:
 * - int[] nums1: a non-empty array of integers
 * - int[] nums2: a non-empty array of integers
 *
 * Returns:
 * - boolean: true if nums1 is a permutation of nums2, false otherwise
 *
 * Examples:
 * Input: nums1 = [1, 2, 3], nums2 = [3, 2, 1]
 * Output: true
 *
 * Input: nums1 = [1, 2, 2], nums2 = [2, 1, 1]
 * Output: false
 *
 * Input: nums1 = [4, 5, 6], nums2 = [4, 6, 5]
 * Output: true
 *
 * Constraints:
 * - 1 <= nums1.length, nums2.length <= 10^4
 * - -10^6 <= nums1[i], nums2[i] <= 10^6
 */

// create a class cc22
// inside the class declare the main method
// public static void main(String[] args) {
//       int[] nums1 = {1, 2, 3, 41, 5};
//       int[] nums2 = {1, 2, 3, 41, 5};
//       System.out.println(findPermutations(nums1, nums2));
//}
//declare a method findPermutations() of boolean type passing in 2 parameters int[] nums1 and int[] nums2
//public static boolean findPermutations(int[] nums1, int[] nums2) {
//      create a new list numList2 set to = Arrays.stream(nums2).boxed().collect(Collectors.toList());
//      List<Integer> numList2 = Arrays.stream(nums2).boxed().collect(Collectors.toList());
//      use an if statement to check the length of both parameters
//      if (nums1.length != nums2.length) {
//          when Not true return false 
//          return false;
//      }
//      use a for each loop to check the elements inside nums1
//      for (int num : nums1) {
//          use a second if statement to check the condition numList2 does NOT contain num --> (!numList2.contains(num))
//          if (!numList2.contains(num)) {
//              return false;
//          } else {
//              remove num from numList2 using .remove() and passing in --> Integer.valueOf(num)
//              numList2.remove(Integer.valueOf(num));
//          }
//      }
//      return false
//  }
//}
import java.util.*;
import java.util.stream.Collectors;

public class cc22 {
    public static void main(String[] args) {
        int[] nums1 = {4, 5, 6};
        int[] nums2 = {4, 6, 5};
        System.out.println(findPermutations(nums1, nums2));
    }
    public static boolean findPermutations(int[] nums1, int[] nums2) {
        List<Integer> numList2 = Arrays.stream(nums2).boxed().collect(Collectors.toList());
        if (nums1.length != nums2.length) {
            return false;
        }
        for (int num : nums1) {
            if (!numList2.contains(num)) {
                return false;
            } else {
                numList2.remove(Integer.valueOf(num));
            }
        }
        return true;
    }
}

