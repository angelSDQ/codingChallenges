/*
LeetCode-style Problem: Longest Word in Sentence

Given a sentence s, return the longest word in the sentence.

If there are multiple words with the same maximum length, return the first one that appears.

Parameters:
    s (String): A non-empty string consisting of lowercase and/or uppercase English letters and spaces only.

Returns:
    String: The longest word in the sentence.

Examples:
    Input: s = "I love abandonments of artificial intelligence"
    Output: "artificial"

    Input: s = "a bc def"
    Output: "def"

Constraints:
    - 1 <= s.length <= 10^5
    - s contains only letters and spaces
    - s contains at least one word
*/
/*
public class cc8 {
    public static void main(String[] args) {
        String word = findsTheLongestWord("I love abandonments of artificial intelligence");
        System.out.println(word);
    }
    public static String findsTheLongestWord(String s) {
        String theLongestWord = "";
        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++) {
            if (words[i].length() > theLongestWord.length()) {
                theLongestWord = words[i];
            }
        }
    return theLongestWord;
    }
}
*/
// PSEUDOCODE
// declare a function findsTheLongestWord passing one parameter s
// function findsTheLongestWord(s) {
//      declare a variable theLongestWord of let type and set equal to empty string ""
//      let theLongestWord = ""
//      declare a variable named words of let type and set equal to s.split(" ")
//      let words = s.split(" ")
//      use a for loop to iterate on words using .length on word
//      for (let i = 0; i < word.length; i++) {
//          use an if statement to check for the condition words[i].length > theLongestWord.length
//          if true set theLongestWord = words[i]
//      }
//      return theLongestWord
//}

function findsTheLongestWord(s) {
    let theLongestWord = "";
    let words = s.split(" ");
    for (let i = 0; i < words.length; i++) {
        if (words[i].length > theLongestWord.length) {
            theLongestWord = words[i];
        }
    }
    return theLongestWord;
}

console.log(findsTheLongestWord("I love of artificial intelligence"));