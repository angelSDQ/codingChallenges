# 🧪 Problem: Reverse Words in a Sentence (No Built-in Reverse)
# Difficulty: Easy
# Category: String Manipulation / Two-Pointer
#
# 📝 Description:
# Given a string `s` representing a sentence, return a new string where each
# word is reversed individually, but the order of words and spacing remains the same.
# You must NOT use built-in reverse functions or slicing (e.g., s[::-1]).
#
# A word is defined as a sequence of non-space characters.
# Words are separated by exactly one space. There are no leading or trailing spaces.
#
# 🔧 Constraints:
# • 1 <= s.length <= 10^5
# • s contains only printable ASCII characters (32–126)
# • s consists of words separated by single spaces
#
# 🧠 Input Format:
# - A single string `s`
#
# 🧠 Output Format:
# - A new string with each word reversed individually, preserving word order and spacing
#
# 🔍 Examples:
#
# Example 1:
# Input:  "hello world"
# Output: "olleh dlrow"
#
# Example 2:
# Input:  "ChatGPT is amazing"
# Output: "TPGtahC si gnizama"
#
# Example 3:
# Input:  "reverse every word"
# Output: "esrever yreve drow"
'''
split on string s to get a list of words on space
have a variable to store the final string to return
use for loop to iterate the list of words to grab the individual words
create a reverseMe to store the words
use a second for loop to iterate on reverseMe and grab the individual letters
but stay in the same placement of the sentence
'''

#define a function reversingWords() pass one parameter s
# def reversingWords(s):
#   create a reversedWords variable to store final string set to ""
#   reversedWords = ""
#   split string s on " "
#   words = s.split(" ")
#   use for loop to iterate the list of words to grab the individual words
#   for word in words:
#       create a reverseMe to store the words set to ""
#       reverseMe = ""
#       use second for to grab each letter from word
#       for letter in range(len(word) -1, -1, -1):
#           build word back up add from the left
#           reverseMe += word[i]
#        reverseWords += reverseMe + " "
#   return reverseWords
#
# print call reversingWords()

# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)  outcome: [5, 4, 3, 2, 1]


def reversingWords(s):
    reversedWords = ""
    words = s.split(" ")
    for word in words:
        reverseMe = ""
        for i in range(len(word)-1, -1, -1):
            reverseMe += word[i]
        reversedWords += reverseMe + " "
    return reversedWords

def reversingWords2(s):
    reversedWords = ""
    words = s.split(" ")
    for word in words:
        reversedWords += word[::-1] + " "
    return reversedWords


print(reversingWords("hello ME"))













































































































