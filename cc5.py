# Contains Only Digits
# Given a string s, return true if it contains only digit characters (0-9), and false otherwise.
# Example 1:
# Input: s = "123456"
# Output: true
# Example 2:
# Input: s = "12a3"
# Output: false
# Constraints:
# •	1 <= s.length <= 10⁵
# •	s contains ASCII characters

# SOLUTION

# I have a bag with unknown characters
# and I have a second bag with numbers 0-9
# I have to compare all of characters in the first 
# to all of the content of the second bag
# if my second bag is empty and no match waas found
# false outcome

# Declare a function onlyNumbers and pass string s
#   Declare a variable numsList to hold numbers from 0-9
#   numsList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#   Use a for loop to iterate through string s
#   for i in s:
#       use if statements check if string s holds only numbers by using != not equal to operator
#       if i not in numsList
#           return False
#   return True 
#
# call onlyNumbers("123456"))

def onlyNumbers(s):
    numsList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in s:
        if i not in numsList:
            return False
    return True

print(onlyNumbers("a11563742876347263847628734682763487263467"))