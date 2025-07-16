/**
 * LeetCode-style Problem: Reverse a List
 *
 * Given a list of integers `nums`, return the list in reversed order.
 *
 * Examples:
 * Input: nums = [1, 2, 3]
 * Output: [3, 2, 1]
 *
 * Input: nums = [5]
 * Output: [5]
 * Input: nums = [4, 8, 15, 16, 23, 42]
 * Output: [42, 23, 16, 15, 8, 4]
 *
 * Input: nums = [10, -1, 0, 7]
 * Output: [7, 0, -1, 10]
 *
 * Constraints:
 * - 1 <= nums.length <= 10^5
 * - -10^9 <= nums[i] <= 10^9
 * 
 */
// create a class cc10
// create a main method in the class
// public static void main(String[] args) {
//      int[] numsReversed = reversedLst(nums);
//      for (int i = 0; i < reversedLst.length, i++)
//      System.out.println(numsReversed[i]);
//}
// Declare a method called reversingNums() of type int[] passing 1 parameter of int[] type
// public static int[] reversingNums(int[] nums) {
//     declare a variable numsReversed of int[] type and set equal to new int[nums.length]
//     int[] numsReversed = new int[nums.length];
//     declare a variable idx of int type and set to 0
//     int idx = 0;
//     use a for loop to interate on numsReversed.length in reverse
//     for (int i = nums.length() -1; i >= 0; i--) {
//         set numsReversed[idx] equal to nums[i]
//         numsReversed[idx] = nums[i];
//         increment idx++;
//     }
//     return numsReversed
//}
public class cc10 {
    public static void main(String[] args) {
    int[] nums = { 5, 10, 15, 20, 25, 30, 35, 40, 45};
    int[] numsReversed = reversingNums(nums);
    for (int i = 0; i < numsReversed.length; i++)
    System.out.println(numsReversed[i]);
    }
    public static int[] reversingNums(int[] nums) {
        int[] numsReversed = new int[nums.length];
        int idx = 0;
        for (int i = nums.length -1; i >= 0; i--) {
            numsReversed[idx] = nums[i];
            idx++;
        }
    return numsReversed;
    }
}
