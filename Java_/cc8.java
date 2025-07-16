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
//PSEUDOCODE
// create a class cc8
//      declare the main method inside the class
//      public static void main(String[] args) {}
//      declare a method named findsTheLongestWord() passing one parameter s of String type
//      public static String findsTheLongestWord(String s){}
//          declare a variable theLongestWord of String type and set equal to empty string ""
//          String theLongestWord = "";
//          declare a variable named words of String[] type and set equal to s.split(" ")
//          String[] words = s.split(" ");
//          use a for loop to iterate on words to access each word
//          for (int i = 0; i < words.length(); i++) {
//              use an if statement to check the condition if words[i].length() > theLongestWord.length();
//              if (words[i].length() > theLongestWord.length());
//                  if true then set theLongestWord equal to words
//                  theLongestWord = words[i];
//      call findsTheLongestWord method inside of main method
//      return theLongestWord;


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
