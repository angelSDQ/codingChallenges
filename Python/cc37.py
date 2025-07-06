"""
🔎 Problem 11: First Non-Repeating Consonant (Ignore Vowels and Digits)  
Difficulty: Easy–Medium  
Category: String Traversal / Hashing / Filtering

📝 Description:  
Given a string `s`, return the **index** of the first non-repeating **consonant** character.  
Ignore all vowels (`a`, `e`, `i`, `o`, `u`) and digits (`0–9`).  
If no consonant appears exactly once, return -1.

🔧 Constraints:  
• 1 <= len(s) <= 10⁵  
• `s` contains lowercase English letters and digits only

🧠 Input Format:  
- A single string `s`

🧠 Output Format:  
- An integer: the index of the first non-repeating consonant, or -1 if none exists

🔍 Examples:

Example 1:  
Input: s = "leetcode123"  
Output: 0  
Explanation: Ignore vowels ('e', 'e', 'o', 'e') and digits ('1', '2', '3').  
Consonants: l (0), t (3), c (4), d (6) — all unique.  
'l' at index 0 is the first non-repeating consonant.

Example 2:  
Input: s = "aabbccdd1122"  
Output: -1  
Explanation: Only consonants are b, c, d — all repeated. Digits and vowels are ignored.

Example 3:  
Input: s = "abcabcde"  
Output: 6  
Explanation: Ignore vowels ('a', 'e').  
Consonants: b (1, 4), c (2, 5), d (6) → 'd' at index 6 is the first non-repeating consonant.

Example 4:  
Input: s = "aeiou12345"  
Output: -1  
Explanation: No consonants — only vowels and digits.

Example 5:  
Input: s = "h3he4llo5"  
Output: -1  
Explanation: Consonants: h (0, 2), l (5, 6) — all repeated.  
Digits and vowels ignored. No unique consonant remains.
"""



# define a function nonRepeatingConsonant() and pass one parameter s
# def nonRepeatingConsonant(s):
#     create an empty dictionary wordMap
#     wordMap = {}
#     create list of vowels ["a", "e", "i", "o", "u"]
#     vowels = ["a", "e", "i", "o", "u"]
#     create a list of nums ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     use a for loop to iterate on s string using .lower()
#     for letter in s.lower():
#         use an if statement to check the letter is in the wordMap dictionary if true += 1
#         if letter in wordMap:
#             wordMap[letter] += 1
#         use to set value to one when letter is NOT in the the wordMap dictionary
#         else:
#             wordMap[letter] = 1
#     use a second for loop on s string using range len       
#     for letterIndex in range(len(s)):
#         use an if statement to check the value of wordMap passing word[indexLetter] as the key and s[letterIndex] in vowels and s[letterIndex] not in nums
#         if wordMap[s[letterIndex]] == 1 and s[letterIndex] in vowels and s[letterIndex] not in nums:                      
#             return letterIndex
#     return -1 



def nonRepeatingConsonant(s):
    wordMap = {}
    vowels = ["a", "e", "i", "o", "u"]
    # nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for letter in s.lower():
        if letter in wordMap:
            wordMap[letter] += 1
        else:
            wordMap[letter] = 1
    for letterIndex in range(len(s)):
        if wordMap[s[letterIndex]] == 1 and s[letterIndex] not in vowels and not s[letterIndex].isdigit():                     
            return letterIndex
    return -1  

print(nonRepeatingConsonant("1abcabcde"))