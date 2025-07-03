"""
Problem: Replace Digits with Asterisks
Difficulty: Easy

Given a string s, replace every digit character (0 through 9) with an asterisk (*)
and return the modified string.

Examples:
----------
Input: s = "abc123"
Output: "abc***"

Input: s = "passw0rd123!"
Output: "passw*rd***!"

Constraints:
------------
•  1 <= len(s) <= 1000
•  s may contain letters, digits, punctuation, or symbols
"""

# define a function that takes one parameter s
#def hidesNumbers(s):
#   declare a list of numbers from 0 - 9 
#   numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#   declare modifiedWord string and set to empty ""
#   modifiedWord = ""
#   use a for loop to iterate through s string
#   for i in s:
#       use if statement to check for the condition
#       if i in numbers:
#           modifiedWord += "*"
#       else if no i was a match within numbers return add i to modifiedWord
#       else:
#            modifiedWord += i
#
#   return modifiedWord 
# 
# print(hidesNumbers(s))
          

def hidesNumbers(s):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    modifiedWord = ""
    for i in s:
        if i in numbers:
            modifiedWord += "*"
        else:
            modifiedWord += i
    
    return modifiedWord

print(hidesNumbers("2aksjfkj1shdfkja3"))