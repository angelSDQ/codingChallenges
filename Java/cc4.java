package Java;

//PROBLEM

// Count Vowels
// Given a string s, return the total number of vowels (a, e, i, o, u) in the string.
// Treat uppercase and lowercase vowels as the same.
// Example 1:
// Input: s = "leetcode"
// Output: 4
// Example 2:
// Input: s = "rhythm"
// Output: 0
// Constraints:
// •	1 <= s.length <= 10⁵
// •	s contains printable ASCII characters only

// SOLUTION

// Declare a function vowelsMatch(s):
//   Declare a variable to store the vowels count
//   vowelsCount = 0
//   Declare a list that stores the individual characters in the string
//   vowels = ["a", "e", "i", "o", "u"]
//   Use for loop to iterate throught the string s
//   for i in s.lower():
//       Use if statement to find and count when a vowel and store to vowelsCount
//           if i in vowels:
//               vowelsCount += 1

//   return vowelsCount

public class cc4 {
    public static void main(String[] args) {
        System.out.println(vowelsMatch("Ajsdbsdjbsjb"));
    }
//     public static int vowelsMatch(String word) {
//         char[] vowels = {'a', 'e', 'i', 'o', 'u'};
//         int vowelsCount = 0;
//         for (int i = 0; i < vowels.length; i++) {
//             if (word.toLowerCase().contains(String.valueOf(vowels[i]))) {
//                 System.out.println(vowels[i]);
//                 System.out.println(word);
//                 vowelsCount++;
//             }
//         }
//         return vowelsCount;
//     }
// }

public static int vowelsMatch(String word) {
    char[] vowels = {'a', 'e', 'i', 'o', 'u'};
    int vowelsCount = 0;
    for (int i = 0; i < word.length(); i++) {
        System.out.println(i);
        if (word.toLowerCase().contains(String.valueOf(vowels[i]))) {
            System.out.println(vowels[i]);
            System.out.println(word);
            vowelsCount++;
        }
    }
    return vowelsCount;
}
}