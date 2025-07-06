"""
🧠 Problem: Count Words Containing a Specific Letter
🟧 Difficulty: Medium-Hard
📂 Category: String Manipulation / Character Matching

📝 Description:
Given a string `s` representing a sentence and a character `ch`, return the number of words in `s` that contain the character `ch`. The comparison should be **case-insensitive**.

A word is defined as a sequence of non-space characters separated by one or more spaces. The string may have leading, trailing, or multiple intermediate spaces.

✅ You may use `str.split()`.

---

🔧 Constraints:
• 1 <= len(s) <= 10⁵  
• `s` contains only printable ASCII characters (32–126)  
• `ch` is a single alphabetic character (a–z or A–Z)

---

🔎 Examples:

Example 1:
Input:  
s = "Programming in Python is powerful"  
ch = "p"  
Output: 2  
# Matching words: "Programming", "powerful"

Example 2:
Input:  
s = "  every word here has e "  
ch = "e"  
Output: 3  
# Matching words: "every", "here", "e"

Example 3:
Input:  
s = " This Is Clean "  
ch = "z"  
Output: 0

---

🧠 Input Format:
- A string `s`
- A single character `ch`

🧠 Output Format:
- A single integer: the number of words in `s` that contain `ch` (case-insensitive)
"""

#define a function noRepeatingChars() passing one parameter s
# def noRepeatingChars(s):
# create one variables noDuplicates and set to "" empty string
# noDuplicates = ""
#       use a for loop to iterate on the s to access the individual letters
#       for letter in s:
#           use an if statement and .lower() to check if any of the letters are already store in noDuplicates
#           if letter not in noDuplicates:
#               if true add letter to noDuplicates
#               noDuplicates += letter
#       return noDuplicates



def noRepeatingChars(s):
    noDuplicates = ""
    for letter in s:
        if letter not in noDuplicates:
            noDuplicates += letter
    return noDuplicates

print(noRepeatingChars("murcielago"))