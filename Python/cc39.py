"""
🐍➡️🐫 Problem: Conditional Snake Case to Camel Case  
Difficulty: Easy–Medium  
Category: String Manipulation / Formatting

📝 Description:  
Given a string `s` in `snake_case` format, convert it to `camelCase` with the following rule:  
- If a word has **4 or more characters**, capitalize its first letter.  
- If a word has **fewer than 4 characters**, leave it in lowercase.

Remove all underscores `_` in the final output.

🔧 Constraints:  
• 1 <= len(s) <= 10⁵  
• `s` consists of lowercase English letters and underscores `_` only  
• `s` will not start or end with an underscore, and does not contain consecutive underscores

🧠 Input Format:  
- A string `s` in `snake_case` format

🧠 Output Format:  
- A string in modified camelCase format, based on word length

🔍 Examples:

Example 1:  
Input: s = "convert_this_string"  
Output: "convertThisString"  
Explanation: "convert" (7) → lowercase, "this" (4) → capitalize → "This", "string" (6) → "String"

Example 2:  
Input: s = "it_should_be_easy"  
Output: "itShouldBeEasy"

Example 3:  
Input: s = "do_it_now"  
Output: "doItNow"  
Explanation: "do" and "it" stay lowercase, "now" is capitalized

Example 4:  
Input: s = "keep_this_short"  
Output: "keepThisShort"

Example 5:  
Input: s = "abc_def_ghij"  
Output: "abcDefGhij"
"""

#define a function changeToCamelCase and passing one parameter s
#def changeToCamelCase(s):
#   create a variable camelCaseConvertion and set to empty "" string
#   camelCaseConvertion = ""
#   split string s on "_" and store in word
#   words = s.split("_")
#   use a for range len for loop to iterate on all of the letters from word
#   for i in range(len(words)):
#       use an if statement to set up first condition and isolate the first word use words[i] == 0
#       if i == 0 or len(words[i]) <= 3:
#           use camelCaseConvertion variable to start constructing the new camelCase version and use .lower()
#           camelCaseConvertion += words[i].lower()
#           use an else to setUp second word by isolating the first letter with [i][0] and .upper() to capitalize after slice with [1:] to drop original letter
#       else:
#           camelCaseConvertion += words[i][0].upper() + words[i][1:]
#   return camelCaseConvertion

def changeToCamelCase(s):
    camelCaseConvertion = ""
    words = s.split("_")
    for i in range(len(words)):
        if i == 0 or len(words[i]) <= 3:
            camelCaseConvertion += words[i].lower()
        else:
            camelCaseConvertion += words[i][0].upper() + words[i][1:]
    return camelCaseConvertion

print(changeToCamelCase("abc_def_ghij"))

