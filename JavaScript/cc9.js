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

//declare a function findsTheShortestWord that takes 1 parameter s
//function findsTheShortestWord(s) {
//      declare a variable called words and use .split(" ") to create a list of words
//      let words = s.split(" ");
//      declare a variable shortestWord and set it to words[0]
//      let shortestWord = words[0];
//      use a for loop to iterate on shortestWord.length
//      for (let i = 0; i < words.length; i++) {
//          use an if statement to check condition (words[i].length <= shortestWord.length)
//          if (words[i].length() <= shortestWord.length()) {
//              shortestWord = words[i];
//          }
//      }
//      return shortestWord;
//}

function findsTheShortestWord(s) {
    let words = s.split(" ");
    let shortestWord = words[0];
    for (let i = 0; i < words.length; i++) {
        if (words[i].length <= shortestWord.length) {
            shortestWord = words[i];
        }
    }
    return shortestWord;
}
console.log(findsTheShortestWord("to be or not to mm"));

