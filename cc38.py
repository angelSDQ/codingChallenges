"""
🐍➡️🐫 Problem: Snake Case to Camel Case  
Difficulty: Easy  
Category: String Manipulation / Formatting

📝 Description:  
Given a string `s` in `snake_case` format, convert it to `camelCase` and return the result.  
In `camelCase`, the first word remains lowercase, and every subsequent word starts with an uppercase letter.  
Underscores are removed.

🔧 Constraints:  
• 1 <= len(s) <= 10⁵  
• `s` consists of lowercase English letters and underscores `_` only  
• `s` will not start or end with an underscore, and does not contain consecutive underscores

🧠 Input Format:  
- A single string `s` in snake_case format

🧠 Output Format:  
- A string in camelCase format

🔍 Examples:

Example 1:  
Input: s = "convert_this_string"  
Output: "convertThisString"

Example 2:  
Input: s = "make_it_work"  
Output: "makeItWork"

Example 3:  
Input: s = "justoneword"  
Output: "justoneword"

Example 4:  
Input: s = "snake_case_to_camel_case"  
Output: "snakeCaseToCamelCase"
"""

#define a function wordToCamelCase and passing one parameter s
#def wordToCamelCase(s):
#   create a variable camelCaseWord and set to empty "" string
#   camelCaseWord = ""
#   split string s on "_" and store in word
#   words = s.split("_")
#   use a for range len for loop to iterate on all of the letters from word
#   for i in range(len(words)):
#       use an if statement to set up first condition and isolate the first word use words[i] == 0
#       if words[i] == 0:
#           use camelCaseWord variable to start constructing the new camelCase version and use .lower()
#           camelCaseWord += words[i].lower()
#           use an else to setUp second word by isolating the first letter with [i][0] and .upper() to capitalize after slice with [1:] to drop original letter
#       else:
#           camelCaseWord += words[i][0].upper() + words[i][1:]
#   return camelCaseWord




def wordToCamelCase(s):
    camelCaseWord = ""
    words = s.split("_")
    for i in range(len(words)):
        if i == 0:
            camelCaseWord += words[i].lower()
        else:
            camelCaseWord += words[i][0].upper() + words[i][1:].lower() 
    return camelCaseWord

print(wordToCamelCase("snake_case_to_camel_case"))