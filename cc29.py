"""
Capitalize Long Words
Given a string s, capitalize the first letter of each word **that has more than 3 letters** and return the new string.
Words are separated by spaces.

Example 1:
Input: s = "hello world"
Output: "Hello World"

Example 2:
Input: s = "this is a test"
Output: "This is a Test"

Example 3:
Input: s = "go to the park"
Output: "go to the Park"

Example 4:
Input: s = "an example of modification"
Output: "an Example of Modification"

Constraints:
• 1 <= s.length <= 10⁵
• s contains lowercase letters and spaces only
"""

# define a function capitalizeWord passing in one parameter s
# def capitalizeWord(s):
#       create a variable to hold the modified sentence and sset to empty string ""
#       capitalizingWord = ""
#       split string s on empty space " " store to a variable
#       words = s.split(" ")
#       use a for loop to iterate on list of words
#       for word in words:
#           create a local variable to store the new capitalize word/s
#           firstUpper = ""
#           use an if statement to check if the word is greater than 3 characters using len() method
#           if len(word) > 3:
#               use a for loop to iterate on word using range and len methods
#               for i in range(len(word)):
#                   use an if statement to find the first letter of the word
#                   if i == 0:
#                       capitalize first letter of the word that is longer than 3
#                       firstUpper += word[i].upper()
#                   else:
#                       using the else to finish building back the word with Capitalize letter
#                       firstUpper += word[i]
#                   word = firstUpper
#               capitalizeWord += word + " "
#         return capitalizeWord 


def capitalizeWord(s):
    capitalizeWord = ""
    words = s.split(" ")
    for word in words:
        firstUpper = ""
        if len(word) > 3:
            for i in range(len(word)):
                if i == 0:
                    firstUpper += word[i].upper()
                else:
                    firstUpper += word[i]
            word = firstUpper
        capitalizeWord += word + " "
    return capitalizeWord 


print(capitalizeWord("an example of modification titanic"))