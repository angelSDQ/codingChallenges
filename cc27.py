# 🧪 Problem: Reverse Words Starting With Vowels (No Built-in Reverse)
# Difficulty: Easy  
# Category: String Manipulation / Conditional Logic  

# 📝 Description:  
# Given a string `s` representing a sentence, return a new string where only the words  
# that start with a vowel (a, e, i, o, u — case-insensitive) are reversed.  
# All other words must remain unchanged. Word order and spacing must be preserved.  

# You must NOT use:
# - Built-in reverse functions
# - Slicing (e.g., word[::-1])

# A word is defined as a sequence of non-space characters.
# Words are separated by exactly one space. No leading or trailing spaces.

# 🔧 Constraints:
# • 1 <= s.length <= 10^5  
# • s contains only printable ASCII characters (32–126)  
# • s consists of words separated by single spaces  

# 🧠 Input Format:  
# - A single string `s`

# 🧠 Output Format:  
# - A new string where only vowel-starting words are reversed  

# 🔍 Examples:

# Example 1:  
# Input:  "apple is tasty and orange"  
# Output: "elppa si tasty dna egnaro"

# Example 2:  
# Input:  "Umbrella under sky is open"  
# Output: "allerbmU rednu sky si nepo"

# Example 3:  
# Input:  "this sentence has no vowel start"  
# Output: "this sentence has no vowel start"

'''
Goals at a glance

Create a function
Reverse words that start with vowels
other words must remain the same
'''

#define a function reverseVowels() pass one parameter s
# def reverseVowels(s): 
#   create variables to hold modified sentence and set to empty string
#   modifiedWords = ""
#   split string s on empty string " " and store to variable words
#   words = s.split(" ")
#   create a list with vowels
#   vowels = ["a", "e", "i", "o", "u"]
#   use a for loop to iterate on the list of words
#   for word in words:
#       use an if statement and word[0].lower() to find the words that start with a vowel and .lower() to handle uppercase
#       if word[0].lower() in vowels:
#           backWordsVowels = ""
#           use a for loop to iterate on word
#           for i in range(len(word)-1, -1, -1):
#               use the local vaariable backWordsVowels to store the reversed words
#               backWordsVowels += word[i]
#           set the new reversed backWordsVowels to word
#           word = backWordsVowels
#       built back the sentence and store in modifiedWords
#       modifiedWords += word + " "
#   return the modifiedWords string
#   return modifiedWords
#
# print call modifiedWords



def reverseVowels(s): 
  modifiedWords = ""
  words = s.split(" ")
  vowels = ["a", "e", "i", "o", "u"]
  for word in words:
      if word[0].lower() in vowels:
          backWordsVowels = ""
          for i in range(len(word)-1, -1, -1):
              backWordsVowels += word[i]
          word = backWordsVowels
      modifiedWords += word + " "
  return modifiedWords

print(reverseVowels("Umbrella under sky is open"))

