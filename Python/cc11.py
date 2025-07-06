"""
Problem: Detect Capital Usage
Difficulty: Easy

Given a word, return True if the usage of capitals in it is correct.

A word is correctly capitalized if:
- All letters are capitalized. (e.g., "USA")
- No letters are capitalized. (e.g., "leetcode")
- Only the first letter is capitalized. (e.g., "Google")

Otherwise, return False.

Examples:
----------
Input: word = "USA"
Output: True

Input: word = "FlaG"
Output: False

Constraints:
------------
- 1 <= len(word) <= 100
- The word contains only English letters
"""

#Pseudocode

# Declare a function correctCapitalization that takes one parameter
# def correctCapitalization(word):
#   use if statement to check the grammar condition using isupper() method
#   if word.isupper():
#       return True
#   use a for loop to iterate on given word
#   for i in range(1, len(word)):
#       use if statement to check the rest of the letters using range to indicate the start and len passing in word to signify the end of paramater
#       if word[i].isupper():
#           return False
#   return True
# 
# print(correctCapitalization("Word"))   



def correctCapitalization(word):
    if word.isupper():
        return True
    for i in range(1, len(word)):
        if word[i].isupper():
            return False
    return True
        
print(correctCapitalization("Google"))