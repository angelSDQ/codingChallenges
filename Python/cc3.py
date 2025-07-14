# PROBLEM

# Count Vowels
# Given a string s, return the total number of vowels (a, e, i, o, u) in the string.
# Treat uppercase and lowercase vowels as the same.
# Example 1:
# Input: s = "leetcode"
# Output: 4
# Example 2:
# Input: s = "rhythm"
# Output: 0
# Constraints:
# •	1 <= s.length <= 10⁵
# •	s contains printable ASCII characters only

# SOLUTION

# Declare a function vowelsMatch(s):
#   Declare a variable to store the vowels count
#   vowelsCount = 0
#   Declare a list that stores the individual characters in the string
#   vowels = ["a", "e", "i", "o", "u"]
#   Use for loop to iterate throught the string s
#   for i in s.lower():
#       Use if statement to find and count when a vowel and store to vowelsCount
#           if i in vowels:
#               vowelsCount += 1

#   return vowelsCount

def vowelsMatch(s):
    vowelsCount = 0
    vowels = ["a", "e", "i", "o", "u"]

    for i in s.lower():
        if i in vowels:
            vowelsCount += 1

    return vowelsCount

print(vowelsMatch('mIssissIpi'))