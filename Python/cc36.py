"""
🧠 Problem 11: First Non-Repeating Vowel  
Difficulty: Easy–Medium  
Category: String Traversal / Hashing / Filtering

📝 Description:  
Given a string `s`, return the **index** of the first non-repeating **vowel** character.  
If there is no such vowel, return -1.  
Only vowels ('a', 'e', 'i', 'o', 'u') should be considered for uniqueness.

🔧 Constraints:  
• 1 <= len(s) <= 10⁵  
• `s` contains only lowercase English letters

🧠 Input Format:  
- A single string `s`

🧠 Output Format:  
- An integer: the index of the first non-repeating vowel character, or -1 if none exists

🔍 Examples:

Example 1:  
Input: s = "leetcode"  
Output: 2  # 'e' at index 2 is the first non-repeating vowel

Example 2:  
Input: s = "aabbcc"  
Output: -1  # 'a' appears more than once, no other vowels

Example 3:  
Input: s = "rhythm"  
Output: -1  # no vowels

Example 4:  
Input: s = "aeiouaei"  
Output: 4  # 'o' at index 4 is the first vowel that appears once
"""
# define a function nonRepeatingVowels() and pass one parameter s
# def nonRepeatingVowels(s):
#     create an empty dictionary wordMap
#     wordMap = {}
#     create list of vowels ["a", "e", "i", "o", "u"]
#     vowels = ["a", "e", "i", "o", "u"]
#     use a for loop to iterate on s string using .lower()
#     for letter in s.lower():
#         use an if statement to check the letter is in the wordMap dictionary if true += 1
#         if letter in wordMap:
#             wordMap[letter] += 1
#         use to set value to one when letter is NOT in the the wordMap dictionary
#         else:
#             wordMap[letter] = 1
#     use a second for loop on s string using range len       
#     for letteridx in range(len(s)):
#         use an if statement to check the value of wordMap passing word[indexLetter] as the key and s[letteridx] in vowels
#         if wordMap[s[letteridx]] == 1 and s[letteridx] in vowels:                        
#             return letteridx
#     return -1 


def nonRepeatingVowels(s):
    wordMap = {}
    vowels = ["a", "e", "i", "o", "u"]
    for letter in s.lower():
        if letter in wordMap:
            wordMap[letter] += 1
        else:
            wordMap[letter] = 1
    for letteridx in range(len(s)):
        if wordMap[s[letteridx]] == 1 and s[letteridx] in vowels: 
            print(s[letteridx])                       
            return letteridx
    return -1 


print(nonRepeatingVowels("abcdabeo"))
