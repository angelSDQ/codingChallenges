# Remove Specific Character
# Given a string s and a character ch, remove all instances of ch from s and return the resulting string.

# You must maintain the original order of the remaining characters.

# Example 1:
# Input: s = "hello", ch = "l"
# Output: "heo"

# Example 2:
# Input: s = "banana", ch = "a"
# Output: "bnn"

# Constraints:

# 1 <= s.length <= 10⁴

# ch is a single lowercase English letter

# s contains only lowercase English letters

# BREAKDOWN

# need a function
# pass in s and ch parameter like in cc6
# for loop to iterate string s
# a way to leave out "ch" when putting the string back together
# compare ch to s(element)
# if ch 

# THIS IS THE SOLUTION
# 
# Define a function pass 2 variables
# declare a local variable
# use a for loop to iterate through the input
# use if statement to determine if ch is a match with any of the letters from the input
# if match is not found add to the variable create before
# return local variable
# print and call function pass 2 inputs to test


def removingLetter(s, ch):
    newString = ""
    for i in s:
        if i != ch:
            newString += i
    return  newString

print(removingLetter("hi, llldoll yllloul wallnt solmle tlea?", "l"))



