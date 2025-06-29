"""
🧪 Problem: Replace Vowels with Unique Symbols

Difficulty: Easy
Category: String Manipulation

Description:
Given a string s, return a new string where every vowel is replaced with a specific symbol:

Vowel Replacement Mapping:
    a / A → '@'
    e / E → '#'
    i / I → '$'
    o / O → '%'
    u / U → '&'

Rules:
•  Replacement is case-insensitive (e.g., 'A' and 'a' both become '@').
•  All non-vowel characters remain unchanged.

Examples:
Input:  "hello world"
Output: "h#ll% w%rld"

Input:  "Beautiful Day"
Output: "B#@&t$f&l D@y"

Input:  "PYTHON"
Output: "PYTH%N"

Constraints:
•  1 <= len(s) <= 10^4
•  s contains only printable ASCII characters

"""

# Define a function replacingVowels() that takes one parameter s 
# def replacingVowels(s):
#   declare a list to store the values that will be used to replace the vowels
#   keys = ["@", "#", "$", "%", "&"]
#   declare a list of vowels
#   vowels = ["a", "e", "i", "o", "u"]
#   declare wordWithSymbols string and set to empty ""
#   wordWithSymbols = ""
#   use a for loop to iterate on s string using the .lower() method to convert the string to all lower case
#   for i in len(s.lower()):
#       if i in vowels:
#           use for loop to iterate the keys list
#           for i in range(len(keys)):
#               wordWithSymbols += keys[i]
#       else:
#           wordWithSymbols += i
#
#    return wordWithSymbols        


# def replacingVowels(s):
#     #keys = ["@", "#", "$", "%", "&"]
#     vowels = ["a", "e", "i", "o", "u"]
#     wordWithSymbols = ""
#     for i in s.lower():
#         if i == "a":
#             wordWithSymbols += "@"
#         elif i == "e":
#             wordWithSymbols += "#"
#         elif i == "i":
#             wordWithSymbols += "$"
#         elif i == "o":
#             wordWithSymbols += "%"
#         elif i == "u":
#             wordWithSymbols += "&"
#         else:
#             wordWithSymbols += i
    
#     return wordWithSymbols

# def replacingVowels(s):
#     vowels = {"a" : "@", "e" : "#", "i" : "$", "o" : "%", "u" : "&"}
#     wordWithSymbols = ""
#     for i in s:
#         if i.lower() in vowels.keys(): 
#             wordWithSymbols += vowels[i.lower()]
#         else:
#             wordWithSymbols += i
        
#     return wordWithSymbols

def replacingVowels(s):
    vowels = {"a" : "@", "e" : "#", "i" : "$", "o" : "%", "u" : "&"}
    return "".join([vowels[i.lower()] if i.lower() in vowels.keys() else i for i in s])

print(replacingVowels("USA"))