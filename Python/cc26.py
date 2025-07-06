# 🧪 Problem: Reverse Curse Words Only (No Built-in Reverse)
# Difficulty: Easy  
# Category: String Manipulation / Conditional Reversal  

# 📝 Description:  
# Given a string `s` representing a sentence, return a new string where only curse words  
# are reversed. All other words must remain unchanged, and spacing/order must be preserved.  

# You may NOT use:
# - Built-in reverse functions
# - Slicing (e.g., word[::-1])

# Curse words are case-insensitive and limited to this list:
# ["damn", "hell", "shit", "fuck"]

# A word is defined as a sequence of non-space characters.
# Words are separated by exactly one space. No leading or trailing spaces.

# 🔧 Constraints:
# • 1 <= s.length <= 10^5  
# • s contains only printable ASCII characters (32–126)  
# • s consists of words separated by single spaces  
# • Curse words appear in lowercase or uppercase, but must be reversed in their original case  

# 🧠 Input Format:  
# - A single string `s`

# 🧠 Output Format:  
# - A new string where curse words are reversed (in-place), others untouched  

# 🔍 Examples:

# Example 1:  
# Input:  "what the hell is this shit"  
# Output: "what the lleh is this tihs"

# Example 2:  
# Input:  "no need to say fuck or damn"  
# Output: "no need to say kcuf or nmad"

# Example 3:  
# Input:  "he said HELL no and walked off"  
# Output: "he said LLEH no and walked off"


# define a function reversingSentence() passing 1 parameter
# def reversingSentence():
#   create a variable and set to " "
#   reversedSentence = ""
#   split the string s parameter on empty " " and store to variable words
#   words = s.split(" ")
#   use a for loop to iterate on words to get the individual words
#   for word in words:
#       create local variable to keep track of the individual words
#       backWords = " "
#       for i in range(len(word)-1, -1, -1):
#           backWords += word[i]
#       reversedSentence += backWords + " "
#   return reversedSentence

# print call reversingSentence()



def reversingBadWords(s):
    reversedWord = ""
    wordToReverse = ["damn", "hell", "shit", "fuck"]
    words = s.split(" ")
    for word in words:
        if word.lower() in wordToReverse:
            backWords = ""
            for i in range(len(word)-1, -1, -1):
                backWords += word[i]
            word = backWords
        reversedWord += word + " "
    return reversedWord


print(reversingBadWords("no need to say fuck or damn"))




#     for word in words:
#         if word[-1] in punctuationList:
#             punctuationToAddBack = word[-1]
#             print(punctuationToAddBack, " - punctuation test")
#             word = word[:-1]
#             print(word, " - word to bleep test")
#         if word.lower() in wordToBleep:
#             word = word[0] + (len(word[1:-1])) * "*" + word[-1]
#         print(word, " - test for word")
#         censoredSentence += word + punctuationToAddBack + " "
#         print(censoredSentence, " - final sentence test")
#     return censoredSentence