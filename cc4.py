# PROBLEM

# Remove Spaces
# Given a string s, return the string with all space characters removed.
# Example 1:
# Input: s = "remove all spaces"
# Output: "removeallspaces"
# Example 2:
# Input: s = " no space "
# Output: "nospace"
# Constraints:    
# •	1 <= s.length <= 10⁵
# •	s contains printable ASCII characters only

# SOLUTION

# Declare a function removeSpaces(s):
#   Use for loop to iterate throught the string s
#   declare variable to hold word with no spaces
#   noSpacesString = ""
#   for i in s:
#       use if statement 
#       if i != " ":
#          noSpacesString = noSpacesString + i
#
#   return noSpacesString
#
# call removeSpaces

def removeSpaces(s):
    noSpacesString = ""
    for i in s:
        if i != " ":
            noSpacesString = noSpacesString + i

    return noSpacesString 

print(removeSpaces('H               E               L   L                                           O'))