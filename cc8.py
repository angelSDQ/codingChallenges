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

# I have a bag of letters and a letter that I want to find
# in the bag. I need pull all of the letters out of the bag
# to make sure i dont miss any letters. 
# Any time a letter is a match to the letter i'm looking for, 
# I will remove it and save the letters that are not a 
# match to a new bag to return it back. 


# like removing a space but this case is a specific character

# SOLUTION
# 