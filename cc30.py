"""
🧠 Problem: Count Non-Numeric-Starting Words
🟧 Difficulty: Medium-Hard
📂 Category: String Manipulation / Parsing

📝 Description:
Given a string `s` representing a sentence, return the number of words that **do not start with a digit** (0–9).
A word is defined as a sequence of non-space characters separated by one or more spaces. Words may include digits, letters, or symbols.
The string may contain leading, trailing, or multiple intermediate spaces.
✅ You may use `str.split()`.

---
🔧 Constraints:
• 1 <= len(s) <= 10⁵
• `s` contains only printable ASCII characters (32–126)
---

🔎 Examples:
Example 1:
Input: s = "  123abc apple 0xFF orange " Output: 2  
# Words: ["123abc", "apple", "0xFF", "orange"]
# Words not starting with digit: "apple", "orange" → count = 2

Example 2:
Input: s = "99bottles of beer 4the road" Output: 3
# "of", "beer" start with letters

Example 3:
Input: s = " one two three " Output: 3
 # All start with non-digits

Example 4:
Input: s = " 42 314 7eleven " Output: 0 
# All start with digits

---

🧠 Input Format:
- A single string `s`

🧠 Output Format:
- A single integer: the number of words that do **not** start with a digit
"""

# define a function wordsWithNoNums() and pass one parameter s
# def wordsWithNoNums(s):
#   declare a list of numbers from 0-9 and save to nums
#   nums =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#   create a counter and set to 0 to keep track of the valid words
#   count = 0
#   create a variable words and use strip method to trim the ends and Split on empty space " " to get the individual words
#   words = s.strip().split(" ")
#   use a for loop to iterate words 
#   for word in words:
#       use an if statement, word[0] and the nums variable to check the first character of each of the words, to find the ones that start with a number
#       if word[0] not in nums:
#           when the first character or word[0] is not in nums the count will go up by 1
#           count += 1
#   return count




def wordsWithNoNums(s):
    nums =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    count = 0
    words = s.strip().split(" ")
    for word in words:
        if word[0] not in nums:
            count += 1
    return count

print(wordsWithNoNums("  123abc apple 0xFF orange "))