"""
🔍 Problem 11: First Non-Repeating Character  
Difficulty: Easy–Medium  
Category: String Traversal / Hashing

📝 Description:  
Given a string `s`, return the **index** of the first non-repeating character.  
If no such character exists, return -1.

🔧 Constraints:  
• 1 <= len(s) <= 10⁵  
• `s` contains only lowercase English letters

🧠 Input Format:  
- A single string `s`

🧠 Output Format:  
- An integer: the index of the first non-repeating character, or -1 if none exists

🔍 Examples:

Example 1:  
Input: s = "leetcode"  
Output: 0  
Explanation: 'l' is the first character that only appears once.

Example 2:  
Input: s = "aabb"  
Output: -1  
Explanation: All characters repeat.

Example 3:  
Input: s = "loveleetcode"  
Output: 2  
Explanation: 'v' is the first character that only appears once.

Example 4:  
Input: s = "aabbc"  
Output: 4  
Explanation: 'c' is the first non-repeating character.

Example 5:  
Input: s = "abcabcde"  
Output: 6  
Explanation: 'd' is the first character that only appears once.

Example 6:  
Input: s = "z"  
Output: 0  
Explanation: Single character is by default non-repeating.
"""

# define a function called nonRepeatingLetters() and pass one parameter s
# def nonRepeatingLetters(s):
# create an empty dictionary letterIndex  
# wordMap = {}
# use a for loop to iterate on s using .lower() 
# for letter in s.lower():
#   POPULATING THE DICTIONARY letterIndex
#   use an if statement to check if letter is in letterIndex dictionary
#   if letter in wordMap:
#       if true increment the value of the letter using += 1
#       wordMap[letter] += 1
#   else if NOT True letterIndex dict. set the value to 1
#   else:
#       wordMap[letter] = 1
# use a second for loop to iterate on the idx of string s using range(len(s)) passing s
# for letteridx in range(len(s)):
#   using an if statement check if the value of the keys are equal == to 1 passing s[letteridx] to wordMap as the key
#   if wordMap[s[letteridx]] == 1: 
#         return letteridx
# return -1 


def nonRepeatingLetters(s):
    wordMap = {}
    for letter in s.lower():
        if letter in wordMap:
            wordMap[letter] += 1
        else:
            wordMap[letter] = 1
    for letteridx in range(len(s)):
        if wordMap[s[letteridx]] == 1:                        
            return letteridx
    return -1 

print(nonRepeatingLetters("hello"))
