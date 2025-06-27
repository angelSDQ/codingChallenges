# Count Words
# Given a string s, count how many words it contains. Words are separated by one or more spaces.
# Example 1:
# Input: s = "Hello world"
# Output: 2
# Example 2:
# Input: s = " Count the words here "
# Output: 4
# Constraints:
# •	1 <= s.length <= 10⁵
# •	s may contain leading or trailing spaces

# iterate through the string
# use a counter to count words
# use the split method to remove the spaces between the words
# store words in a variable and keep track of the count

# Define a function
# declare a counter set to 0
# use a for loop
# for i in s.split(" "):
#   counter += 1
# 
#   return counter

# print(count_word(""))

def count_word(s):
    counter = 0
    for i in s.split(" "):
        counter += 1

    return counter

print(count_word("Hello world, this function can count words"))



