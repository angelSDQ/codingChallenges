// ✅ Problem: Pangram Check
// 🟨 Difficulty: Easy
// 📂 Category: String / Hash Set

// 📝 Description:
// Given a sentence s, return True if the sentence is a *pangram*, i.e., it contains every letter of the English alphabet 
// at least once. 
// Otherwise, return False.
// Ignore case when checking for presence of each letter.

// 🔒 Constraints:
// • 1 <= s.length <= 10^5
// • s consists of English letters and spaces only

// 🔧 Input Format:
// •  A single string s

// 📤 Output Format:
// •  A boolean value: True if s is a pangram, False otherwise

// 🧪 Examples:
// Example 1:
// Input: s = "The quick brown fox jumps over the lazy dog"
// Output: True
// Example 2:
// Input: s = "Hello world"
// Output: False

// Pseudocode

// Define a function called checkingForPangram() passing one parameter s
// def checkingForPangram(s):
//   create a variable alphabet and set to a list with a-z 
//   alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
//   use a for loop to iterate on the list of letters 
//   for letter in alphabet:
//       use an if statement to check if the letter is not in s 
//       if letter not in s:
//           return False
//   return True

// TIME       Java

public class cc3 {
    public static void main(String[] args) {
        System.out.println(checkingForPangram("The quick BRowN fox jumps over the lazy dog"));
    }
    public static boolean checkingForPangram(String inputS) {
        char[] alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        for (int i = 0; i < alphabet.length; i++) {
            if (!inputS.toLowerCase().contains(String.valueOf(alphabet[i]))) {
                return false;
            }
        }
        return true;
    } 
}
