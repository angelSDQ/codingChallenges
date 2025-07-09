
# LeetCode-style Problem: Longest Word in Sentence

# Given a sentence s, return the longest word in the sentence.

# If there are multiple words with the same maximum length, return the first one that appears.

# Parameters:
#     s (String): A non-empty string consisting of lowercase and/or uppercase English letters and spaces only.

# Returns:
#     String: The longest word in the sentence.

# Examples:
#     Input: s = "I love abandonments of artificial intelligence"
#     Output: "artificial"

#     Input: s = "a bc def"
#     Output: "def"

# Constraints:
#     - 1 <= s.length <= 10^5
#     - s contains only letters and spaces
#     - s contains at least one word

# JAVA
    # public static void main(String[] args) {
    #     String word = findsTheLongestWord("I love abandonments of artificial intelligence");
    #     System.out.println(word);
    # }
    # public static String findsTheLongestWord(String s) {
    #     String theLongestWord = "";
    #     String[] words = s.split(" ");
    #     for (int i = 0; i < words.length; i++) {
    #         if (words[i].length() > theLongestWord.length()) {
    #             theLongestWord = words[i];
    #         }
    #     }
    # return theLongestWord;

# PYTHON TRANSLATION
# define a function findsTheLongestWord that takes one parameter s
# def findsTheLongestWord(s):
#   declare a variable theLongestWord and set equal to empty string ""
#   theLongestWord = ""
#   declare a variable words and set to s.split(" ") to get a list of words
#   words = s.split(" ")
#   use a for loop to iterate on words to access each individual word in words
#   for word in words:
#       use an if statement to check the condition len(word) > len(theLongestWord)
#       if len(word) > len(theLongestWord):
#           if true set theLongestWord = word
#           theLongestWord = word
#   return theLongestWord
# 
# print call function


def findsTheLongestWord(s):
    theLongestWord = ""
    words = s.split(" ")
    for word in words:
        if len(word) > len(theLongestWord):
            theLongestWord = word
    return theLongestWord

print(findsTheLongestWord("a bjhkc def"))