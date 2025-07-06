"""
🔤 Problem: Title Case Excluding Short Words  
Difficulty: Easy–Medium  
Category: String Manipulation / Formatting

📝 Description:  
Given a sentence `s` (all lowercase, words separated by spaces), convert it to **title case**  
with the following rules:
- The **first word** is always capitalized.
- Other words are **only capitalized if they are 4 or more letters long**.
- Words shorter than 4 letters (excluding the first word) remain in lowercase.

🔧 Constraints:  
• 1 <= len(s) <= 10⁵  
• `s` consists of lowercase English letters and single spaces only  
• No leading or trailing spaces, no multiple spaces between words

🧠 Input Format:  
- A single string `s`

🧠 Output Format:  
- The formatted string in modified title case

🔍 Examples:

Example 1:  
Input: s = "make it work now"  
Output: "Make it Work now"

Example 2:  
Input: s = "this is a test sentence"  
Output: "This is a Test Sentence"

Example 3:  
Input: s = "an example of good formatting"  
Output: "An example of Good Formatting"

Example 4:  
Input: s = "try it out and see"  
Output: "Try it out and See"
"""

# define a function titleCaseWord() passing one parameter s
# def titleCaseWord(s):
#     create a variable titleCase and set it to empty string ""   
#     titleCase = ""
#     split string s on empty " " space store in variable words
#     words = s.split(" ")
#     use a for loop to iterate on words using range len
#     for i in range(len(words)):
#         use an if statement to check 2 conditions if i == 0 or len(words[i]) >= 4
#         if i == 0 or len(words[i]) >= 4:          
#             titleCase += words[i][0].upper() + words[i][1:] + " "
#         use else to make the word lowercase with .lower() when they are less than 4
#         else:
#             titleCase += words[i].lower() + " "
#     return titleCase


def titleCaseWord(s):
    titleCase = ""
    words = s.split(" ")
    for i in range(len(words)):
        if i == 0 or len(words[i]) >= 4:          
            titleCase += words[i][0].upper() + words[i][1:] + " "
        else:
            titleCase += words[i].lower() + " "
    return titleCase


print(titleCaseWord("An example of Good Formatting"))