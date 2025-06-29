"""
🔒 Problem: Mask All But Last Four

Difficulty: Easy  
Category: String Manipulation / Masking

Description:
Given a string s, return a new string where *all characters except the last four* are replaced with the character '*'.

Use this to simulate hiding sensitive data like credit card numbers, phone numbers, or IDs.

Examples:
Input:  "1234567890"
Output: "******7890"

Input:  "abcdef"
Output: "**cdef"

Input:  "1234"
Output: "1234"

Input:  "hi"
Output: "hi"

Constraints:
•  1 <= len(s) <= 100
•  s contains only alphanumeric characters and symbols

"""

# define a function maskingString() and pass one parameter s
# def maskingString(s): 
#   create variable maskedWord set to empty string
#   maskedWord = ""
#   create variable unMasked set to empty string
#   unMasked = ""
#   create variable masked set to empty string
#   masked = ""
#   use if statement and len() method pass string s to check if less than or equal to 4
#   if len(s) <= 4:
#       return s
#   use elfi to check the len of s
#       elif len(s) > 4:
#           set values to unMasked and masked
#           unMasked = s[-4:]
#           masked = s[:-4]
#       use for loop to iterate on masked
#       for i in masked:
#           maskedWord += "*"
#       concatenate maskedWord + unMasked
#       return maskedWord + unMasked

# print(maskingString())

'''
Learning leasson

Don't start code from scratch
try to understand why the
code is not working. Try to
understand the logic of the 
code go line by line. Print
test the lines code as you
built the code.
'''


def maskingString(s):
    maskedWord = ""
    unMasked = ""
    masked = ""
    if len(s) <= 4:
        return s
    elif len(s) > 4:
        unMasked = s[-4:]
        masked = s[:-4]
    for i in masked:
        maskedWord += "*"
    return maskedWord + unMasked
    

print(maskingString("89xsdsds0"))