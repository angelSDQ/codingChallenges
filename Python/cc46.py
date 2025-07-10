# LeetCode-style Problem: Shortest Word in Sentence

# Given a sentence s, return the shortest word in the sentence.

# If there are multiple words with the same minimum length, return the last one that appears.

# Parameters:
#     s (String): A non-empty string consisting of lowercase and/or uppercase English letters and spaces only.

# Returns:
#     String: The shortest word in the sentence.

# Examples:
#     Input: s = "The sun is bright"
#     Output: "is"

#     Input: s = "a bc def"
#     Output: "a"

#     Input: s = "to be or not to be"
#     Output: "be"

# Constraints:
#     - 1 <= s.length <= 10^5
#     - s contains only letters and spaces
#     - s contains at least one word



# declare a function findsTheShortestWord() passing 1 parameter s 
# def findsTheShortestWord(s):
#       declare a variable called words and set to s.split(" ") to store a list of words in word
#       words = s.split(" ")
#       declare a variable called shortestWord set equal to empty ""
#       shortestWord = words[0]
#       use a for loop to iterate on words using len()
#       for i in range(len(words)):
#           use an if statement to check the condition len(words[i]) <= len(shortestWord):
#           if len(words[i]) <= len(shortestWord):
#               set shortestWord to words[i]
#               shortestWord = words[i]
#      return shortestWord; 



def findsTheShortestWord(s):
    words = s.split(" ")
    shortestWord = words[0]
    for i in range(len(words)):
        if len(words[i]) <= len(shortestWord):
            shortestWord = words[i]
    return shortestWord 

print(findsTheShortestWord("a bc def"))