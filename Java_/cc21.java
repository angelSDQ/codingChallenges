/**
 * LeetCode-style Problem (Easy-Medium): Find Non-Common Elements Between Two Arrays
 *
 * Given two integer arrays nums1 and nums2, return a new array containing all the unique
 * numbers that appear in only one of the two arrays (i.e., not shared between them).
 * The result should not contain duplicates, and the order of elements does not matter.
 *
 * Parameters:
 * - int[] nums1: A non-empty array of integers
 * - int[] nums2: A non-empty array of integers
 *
 * Returns:
 * - int[]: An array of integers that are unique to either nums1 or nums2 (but not both)
 *
 * Examples:
 * Input: nums1 = [1, 2, 3], nums2 = [2, 3, 4]  
 * Output: [1, 4]
 *
 * Input: nums1 = [5, 6, 7], nums2 = [7, 8, 9]  
 * Output: [5, 6, 8, 9]
 *
 * Input: nums1 = [1, 1, 2], nums2 = [2, 3]  
 * Output: [1, 3]
 *
 * Constraints:
 * - 1 <= nums1.length, nums2.length <= 10^4
 * - -10^6 <= nums1[i], nums2[i] <= 10^6
 */

//IMPORT
//import java.util.Arrays;
// import java.util.List;
// import java.util.Arrays;

//create a class cc21
//inside the class declare a main method 
//public static void main(String[] args) {
//      create variables
//      int[] nums1 = {1, 2, 2, 3};
//      int[] nums2 = {};
//      int[] uniqueNums = findsUniqueNums(nums1, nums2);
//      use a for each loop to iterate on uniqueNums
//      for (int num : uniqueNums) {
//          System.out.println(num);
//      }
//}
//create a method findsUniqueNums() of int[] type passing 2 parameters () int[] nums1 and int[] nums2
//      public static int[] findsUniqueNums(int[] nums1, int[] nums2) {
//          declare a Hashset for numsToKeep
//          Set<Integer> numsToKeep = new HashSet<>();
//          use a for each loop to iterate on nums1
//          for (int num : nums1) {
//              use an if statement to check for the condition (nums2, nums) use Arrays.binarySearch() to use this import  --> java.util.Arrays;
//              if (Arrays.binarySearch(nums2, num) < 0) {
//                  when true populate numsToKeep using .add()
//                  numsToKeep.add(num) 
//              }
//          }
//          use a second loop to iterate on nums2
//          for (int num : nums2) {
//              use an if statement to check for the condition (nums2, nums) use Arrays.binarySearch() to use this import  --> java.util.Arrays;
//              if (Arrays.binarySearch(nums1, num) < 0) {
//                  when true populate numsToKeep using .add()
//                  numsToKeep.add(num) 
//              }
//          }
//          instantiate a variable uniqueNums int[] type and set to new int[numsToKeep.size()];
//          int[] uniqueNums = new int[numsToKeep.size()];
//          declare int i and set to 0
//          int i = 0;
//          use a for each loop to iterate on numsToKeep
//              for (int num : numsToKeep) {
//                  populate numsToKeep using [i]
//                  uniqueNums[i] = num;
//                  i++
//              }
//      return uniqueNums ;
//      }
//}


import java.util.*;

public class cc21 {
    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3};
        int[] nums2 = {2, 3, 4};
        int[] uniqueNums = findsUniqueNums(nums1, nums2);
        for (int num : uniqueNums) {
            System.out.println(num);
    }
}
    public static int[] findsUniqueNums(int[] nums1, int[] nums2) {
        Set<Integer> numsToKeep = new HashSet<>();
        for (int num : nums1) {
            if (Arrays.binarySearch(nums2, num) < 0) {
                numsToKeep.add(num);
            }
        }
        for (int num : nums2) {
            if (Arrays.binarySearch(nums1, num) < 0) {
                numsToKeep.add(num);
            }
        }
        int[] uniqueNums = new int[numsToKeep.size()];
        int i = 0;
        for (int num : numsToKeep) {
            uniqueNums[i] = num;
            i++;
        }
    return uniqueNums ;
    }
}
