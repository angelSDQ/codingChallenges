"""Reverse String
Given a string s, return the string reversed.
You must build the reversed string without using the built-in reverse() method.
Example 1:
Input: s = "hello"
Output: "olleh"
Example 2:
Input: s = "ChatGPT"
Output: "TPGtahC"
Constraints:
•	1 <= s.length <= 10⁵
•	s contains printable ASCII characters only
"""

# declare a function reversingWords() and pass 1 parameter s
# def reversingWords(s):
#   declare variable revervedString and set to ""
#   revervedString = ""
#   use a for loop to iterate on s string 
#   for i in range(len(s)-1, -1, -1):
#       use a local variable revervedString to store the reversed order using word[i] to access each element
#       revervedString += s[i]
#   return revervedString

# print call function

def reversingWords(s):
    revervedString = ""
    for i in range(len(s)-1, -1, -1):
        revervedString += s[i]
    return revervedString

def reversingWords2(s):
    return s[::2]


print(reversingWords2("You must build the reversed string without using the built-in reverse() method"))