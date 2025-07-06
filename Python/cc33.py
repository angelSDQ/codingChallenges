"""
🧹 Problem: Remove Repeated Words  
Difficulty: Easy-Medium  
Category: String Manipulation / Word Filtering

📝 Description:  
Given a sentence `s`, remove all repeated words and return the sentence containing only the **first occurrence** of each word.  
Preserve the original word order.

🔧 Constraints:  
• 1 <= s.length <= 10⁵  
• `s` consists of lowercase English letters and single spaces between words  
• No leading or trailing spaces  

🧠 Input Format:  
- A single string `s` representing a sentence

🧠 Output Format:  
- A new string with duplicate words removed, preserving only their first occurrence

🔍 Examples:

Example 1:  
Input: s = "this is a test this is only a test"  
Output: "this is a test only"

Example 2:  
Input: s = "hello world hello"  
Output: "hello world"

Example 3:  
Input: s = "keep it simple keep it clean"  
Output: "keep it simple clean"

Example 4:  
Input: s = "one two three"  
Output: "one two three"
"""

# define a function called noRepeatingWords that takes one parameter s
# def noRepeatingWords(s):
#     create a variable result to return the modifies string
#     result = ""
#     split string s on empty space " " to access the individual words
#     words = s.split(" ")
#     use a for loop to iterate on words' individual words 
#     for word in words:
#       use an if statement and .lower() method to check if the word is already being store in result
#       if word.lower() not in result:
#           result += word
#     return result



def noRepeatingWords(s):
    result = ""
    words = s.split(" ")
    for word in words:
        if word.lower() not in result:
            result += word + " "
    return result

print(noRepeatingWords("hello world HELLO"))