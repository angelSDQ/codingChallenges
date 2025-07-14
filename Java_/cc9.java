package Java;
/*
LeetCode-style Problem: Shortest Word in Sentence

Given a sentence s, return the shortest word in the sentence.

If there are multiple words with the same minimum length, return the last one that appears.

Parameters:
    s (String): A non-empty string consisting of lowercase and/or uppercase English letters and spaces only.

Returns:
    String: The shortest word in the sentence.

Examples:
    Input: s = "The sun is bright"
    Output: "is"

    Input: s = "a bc def"
    Output: "a"

    Input: s = "to be or not to be"
    Output: "be"

Constraints:
    - 1 <= s.length <= 10^5
    - s contains only letters and spaces
    - s contains at least one word
*/

// declare a class cc9
//  declare a main method inside the class
//  public static void main(String[] args){
//      //call method here
//  declare a method called findsTheShortestWord() passing 1 parameter s DONT FORGET to ADD RETURN TYPE
//  public static String findsTheShortestWord(s) {
//  declare a variable called words and set to s.split(" ") to store a list of words in word
//  String[] words = s.split(" ");
//  declare a variable called shortestWord set equal to empty ""
//  String shortestWord = words[0];
//  use a for loop to iterate on words using .length
//  for (int i = 0; i < words.length; i++ ) {
//      use an if statement to check the condition (words[i].length() <= shortestWord.length())
//      if (words[i].length() <= shortestWord.length()) {
//          shortestWord = words[i];
//      }
//  }
//  return shortestWord; 
//  CALL METHOD INSIDE THE MAIN METHOD
//}
//}
public class cc9 {
    public static void main(String[] args) {
        String shortWord = findsTheShortestWord("this is a big, big house.");
        System.out.println(shortWord);
    }
    public static String findsTheShortestWord(String s) {
        String[] words = s.split(" ");
        String shortestWord = words[0];
        for (int i = 0; i < words.length; i++ ) {
            if (words[i].length() <= shortestWord.length()) {
                shortestWord = words[i];
            }
        }
    return shortestWord;
    }
}