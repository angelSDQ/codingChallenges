/**
 * LeetCode-style Problem (Easy-Medium): Find Common Elements in Two Arrays
 *
 * Given two arrays of integers nums1 and nums2, return a new array containing 
 * all the unique numbers that appear in both arrays. The result can be returned 
 * in any order.
 *
 * Parameters:
 * - int[] nums1: A non-empty array of integers
 * - int[] nums2: A non-empty array of integers
 *
 * Returns:
 * - int[]: An array of integers that are common to both nums1 and nums2, with no duplicates
 *
 * Examples:
 * Input: nums1 = [1, 2, 2, 3], nums2 = [2, 3, 4]  
 * Output: [2, 3]
 *
 * Input: nums1 = [4, 5, 6], nums2 = [1, 2, 3]  
 * Output: []
 *
 * Input: nums1 = [1, 1, 1], nums2 = [1, 1]  
 * Output: [1]
 *
 * Constraints:
 * - 1 <= nums1.length, nums2.length <= 10^4
 * - -10^6 <= nums1[i], nums2[i] <= 10^6
 */

//IMPORT
//import java.util.Arrays;
// import java.util.List;
// import java.util.Arrays;

// create a class cc20
// inside the class create a main method
//      public static void main(String[] args) {
//          create variables
//          int[] nums1 = {1, 2, 2, 3};
//          int[] nums2 = {};
//          int[] matchesFound = findingMatchingNumsInArray(nums1, nums2);
//          use a for each loop to iterate on matchesFound
//          for (int num : matchesFound) {
//              System.out.println(num);
//          }
//      }
//      create a method findingMatchingNumsInArray() of int[] type passing 2 parameters () int[] nums1 and int[] nums2
//      public static int[] findingMatchingNumsInArray(int[] nums1, int[] nums2) {
//          declare an array list for commonNumsInArrays
//          List<Integer> commonNumsInArrays = new ArrayList<>();
//          use a for each loop to iterate on nums1
//          for (int num : nums1) {
//              use an if statement to check for the condition (nums2, nums) use Arrays.binarySearch() to use this import  --> java.util.Arrays;
//              if (Arrays.binarySearch(nums2, num) >= 0) {
//                  when true populate commonNumsInArrays using .add()
//                  commonNumsInArrays.add(num) 
//              }
//          }
//          instantiate a variable matchesFound int[] type and set to new int[commonNumsInArrays.size()];
//          int[] matchesFound = new int[commonNumsInArrays.size()];
//          for (int i = 0; i < commonNumsInArrays.size(); i++) {
//              populate matchesFound using [i] and get(i)
//              matchesFound[i] = commonNumsInArrays.get(i);
//          }
//      return matchesFound;
//      }

import java.util.*;

public class cc20 {
    public static void main(String[] args) {
        int[] nums1 = {1, 2, 2, 3};
        int[] nums2 = {2, 3, 4};
        int[] matchesFound = findingMatchingNumsInArray(nums1, nums2);
        for (int num : matchesFound) {
            System.out.println(num);
        }
    }
    public static int[] findingMatchingNumsInArray(int[] nums1, int[] nums2) {
        Set<Integer> commonNumsInArrays = new HashSet<>();
        for (int num : nums1) {
            if ((Arrays.binarySearch(nums2, num) >= 0)) {
                commonNumsInArrays.add(num);
            }
        }
        int[] matchesFound = new int[commonNumsInArrays.size()];
        int i = 0;
        for (int num : commonNumsInArrays) {
            matchesFound[i] = num;
            i++;
        }
    return matchesFound;
    }
}
