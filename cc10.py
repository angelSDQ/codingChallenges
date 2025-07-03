# Problem:
# Given a string s consisting of characters, *, #, and spaces, write a function to replace all occurrences of * and # with a space character.

# Example:

# Input: s = "Hello*World#!"
# Output: "Hello World !"

# Constraints:

# •    1 <= s.length <= 10^4
# •    s consists of the characters *, #, letters, and spaces.

# create 2 variables to store * and #
# asterisk = *
# poundSign = #

# declare variable set to ""
#newString = ""

#define a function
# def replaceWithSpace():

#use for loop to iterate through string s
# for i in s:

# use an if statement 
#   if i == asterisk or i == poundSign:
#       newString += " "
#   else
#       newString += i

# return newString

# LESSON LEARNED
# look back at all previous coding challenges
# always declare when doing coding challenges
# Don't use methods
# Use for loops, if statements
# Return with correct indentantion
# When declaring variables do it inside 
# of the function to use them later

def replaceWithSpace(s):

    asterisk = "*"
    poundSign = "#"
    newString = ""

    for i in s:
        if i == asterisk or i == poundSign:
            newString += " "
        else:
            newString += i

    return newString

print(replaceWithSpace("Hello*World#!"))