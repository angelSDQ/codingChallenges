"""🤬 Problem: Bleep Swear Words in a Sentence
Difficulty: Medium
Category: String Manipulation / Censorship

📝 Description:
Write a function that receives a string sentence and returns a version where any swear word is censored.

The list of swear words to censor includes (case-sensitive): ["fuck", "shit", "hell", "carajo"]
Each censored word must be transformed as follows:
Keep the first and last character
Replace all characters in between with asterisks *
Maintain the original capitalization of the first and last character
Punctuation attached to the word (like hell. or shit!) must remain at the end, uncensored.

🔧 Constraints:
1 ≤ sentence.length ≤ 1000
Sentence contains printable ASCII characters. Words are separated by spaces. 
Swear words may include ending punctuation (e.g. "shit!")
You may assume punctuation only appears at the end of words

🧠 Input Format:
A single string sentence

🧠 Output Format:
Return the sentence with swear words censored using the described rules.

🔍 Examples:

Example 1:
Input:                          Output:
"What the hell is this shit?"   "What the h**l is this s**t?"

Example 2:
Input:                          Output:
"FUCK that was intense!"        "F**K that was intense!"

Example 3:
Input:                          Output:
"oh shit! that’s bad"           "oh s**t! that’s bad"

Example 4:
Input:                          Output:
"nothing wrong here"            "nothing wrong here"

Example 5:
Input:                          Output:
"hell no, fuck this"            "h**l no, f**k this"
"""

#Pseudocode

#define a function wordBleep() passing 1 parameter sentence
# def wordBleep(sentence):
#   declare variables to store punctuation and to store modified sentence and set to empty string
    # censoredSentence = ""
    # punctuationToAddBack = ""
    # declare a list of all of the special characters that will remain unchanged
    # punctuationList = ["!", "?", ".", ","]
    # declaren list of all words that will be bleeped
    # wordToBleep = ["fuck", "shit", "hell", "carajo"]
    # declare a word variable to store the list of words after spliting sentence parameter
    # word = sentence.split(" ")
    # use for loop on word
    # for i in word:
        # use if to check if any of the words from the word list has a punctuation
        # if i in wordToBleep:
            # store punctuation in punctuationToAddBack
            # punctuationToAddBack = i[-1]
            # firstLttr = i[0]   
            # lastLttr = i[-1]
        # use if statement to handdle cassing
        # if word.lower() in wordToBleep:
            # word[0] + (len(word[1:-1]) * "*") + word[-1]
        # return censoredSentence


def wordBleep(sentence):
    censoredSentence = ""
    punctuationList = ["!", "?", ".", ","]
    punctuationToAddBack = ""
    wordToBleep = ["fuck", "shit", "hell", "carajo"]
    words = sentence.split(" ")
    for word in words:
        if word[-1] in punctuationList:
            punctuationToAddBack = word[-1]
            print(punctuationToAddBack, " - punctuation test")
            word = word[:-1]
            print(word, " - word to bleep test")
        if word.lower() in wordToBleep:
            word = word[0] + (len(word[1:-1])) * "*" + word[-1]
        print(word, " - test for word")
        censoredSentence += word + punctuationToAddBack + " "
        print(censoredSentence, " - final sentence test")
    return censoredSentence

print(wordBleep("What the hell is this shit?"))