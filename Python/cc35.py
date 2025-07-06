"""
🧠 Problem 11: First Unique Character (Ignore Spaces)  
Difficulty: Easy–Medium  
Category: String Traversal / Hashing

📝 Description:  
Given a string `s`, return the **index** of the first non-repeating character **that is not a space**.  
If no such character exists, return -1. Spaces should be ignored during frequency counting.

🔧 Constraints:  
• 1 <= len(s) <= 10⁵  
• `s` contains lowercase letters and spaces only

🧠 Input Format:  
- A single string `s`

🧠 Output Format:  
- An integer: the index of the first non-repeating (non-space) character, or -1 if none exists

🔍 Examples:

Example 1:  
Input: s = "leetcode"  
Output: 0

Example 2:  
Input: s = "a a b b"  
Output: -1

Example 3:  
Input: s = "a b c a b"  
Output: 4  # 'c' is at index 4

Example 4:  
Input: s = "     "  
Output: -1

Example 5:  
Input: s = "z y x y z"  
Output: 4  # 'x' is at index 4
"""

# define a function nonRepeatingChar() passing one parameter s
#def nonRepeatingChar(s):
# create a an empty dictionary wordMap
#   wordMap = {}
#   strip and split on empty space s string safe to a variable word
#   word = s.lower().split(" ")
#   use a for loop to iterate on word
#   for letter in word:
#      use if statement to check if letter in wordMap if yes += 1 to the value
#      if letter in wordMap:
#          wordMap[letter] += 1
#      use else to set the starting value to 1
#      else:
#           wordMap[letter] = 1
#   use a second for loop and iterate on range len of word
#   for indexLetter in range(len(word)):
#       use an if statement to check the value of wordMap passing word[indexLetter] as the key
#       if wordMap[word[indexLetter]] == 1:                        
#           return indexLetter
#   return -1 

def nonRepeatingChar(s):
    wordMap = {}
    word = s.lower()
    for letter in word:
        if letter in wordMap:
            wordMap[letter] += 1
        else:
            wordMap[letter] = 1
    for indexLetter in range(len(word)):
        if wordMap[word[indexLetter]] == 1 and word[indexLetter] != " ":
            return indexLetter
    return -1 

print(nonRepeatingChar("zy xyz"))