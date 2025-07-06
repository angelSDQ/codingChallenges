# Check All Characters Same
# Description:
# Given a string s, return true if all the characters in the string are the same. Otherwise, return false.

# Examples:

# Example 1
# Input:
# s = "aaa"
# Output:
# true
# Explanation:
# All characters are 'a'.

# Example 2
# Input:
# s = "abc"
# Output:
# false
# Explanation:
# The characters are not all the same ('a', 'b', 'c').

# Example 3
# Input:
# s = "bbbbbbbb"
# Output:
# true
# Explanation:
# All characters are 'b'.

# Example 4
# Input:
# s = "c"
# Output:
# true
# Explanation:
# Single-character strings always return true.

# Example 5
# Input:
# s = "ddde"
# Output:
# false
# Explanation:
# The last character is different.


# Define a function pass s
# def repeatingLetters(s)
# use a for loop to iterate through s string index
# for i in range(len(s) -1)
#   s[i]        (current)
#   s[i + 1]    (ahead)
#   s[i - 1]    (behind)
# use if statement to compare i to previous one
    # if s[i] != s[i + 1]:
    #    return False
    # return True   
# Print and call function

def repeatingLetters(s):
    for i in range(len(s)-1):
        if s[i] != s[i + 1]:
            return False
    return True
print(repeatingLetters("mmmmmmmmmmmmmmmmmm"))

    