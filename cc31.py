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

# define a function findMatchingWord() passing two parameters s and ch
# def findMatchingWord(s, ch):
#       create a variable and use strip and split method to store the result
#       words = s.strip().split()
#       use a for loop to iterate through words to get the individual words
#       for word in words:
#           use if statement to check if there is a match with the ch parameter
#           if ch.lower() in word.lower():
#              if true the count will increment by 1
#              count += 1
#       return count 


def findMatchingWord(s, ch):
    words = s.strip().split(" ")
    count = 0
    for word in words:
        if ch.lower() in word.lower():
            print(word, "test")
            count += 1
    return count 

print(findMatchingWord("Programming in Python is powerful", "p"))