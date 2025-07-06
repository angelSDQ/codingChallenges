"""
📝 Capitalize Words

Given a string s, capitalize the first letter of each word and return the new string.
Words are separated by single spaces.

🔧 Constraints:
• 1 <= s.length <= 10⁵
• s contains lowercase letters and spaces only

📥 Example 1:
Input: s = "hello world"
Output: "Hello World"

📥 Example 2:
Input: s = "capitalize me"
Output: "Capitalize Me"

📥 Example 3:
Input: s = "python is fun"
Output: "Python Is Fun"

📥 Example 4:
Input: s = "a quick brown fox"
Output: "A Quick Brown Fox"

📥 Example 5:
Input: s = "x y z"
Output: "X Y Z"

📥 Example 6:
Input: s = "oneword"
Output: "Oneword"
"""

# define a function capitalizeAll() passing one parameter s
# def capitalizeAll(s):
    # create a variable to be use to return the modified sentence and set to empty "" string
    # capitalizeWords = ""
    # split string s on empty " " space to have all individual words
    # words = word.split(" ")
    # use a for loop to iterate on words 
    # for word in words:
    #   create a local variable to store the new capitalize words 
    #   firstUpper = ""
    #   use a second for loop to iterate on the individuals letters from word using range and len
    #   for letter in range(len(word)):
    #       use an if statement to locate the start of each of the words
    #       if i == 0:
    #           set firstUpper to word[i] grabbing that first and with .upper() method capitalize that letter 
    #           firstUpper += word[i].upper()
    #       else if no match was found store the rest as is inside firstUpper
    #       else:
    #           firstUpper = word[i]
    #       use capitalizeWords to store the new modified words stored in firstUpper
    # return capitalizeWords += firstUpper + " "
#  print and call capitalizeWords



def capitalizeAll(s):
    capitalizeWords = ""
    words = s.split(" ")
    for word in words:
        firstUpper = ""
        for i in range(len(word)):
            if i == 0:
                firstUpper += word[i].upper()
            else:
                firstUpper += word[i]   
        capitalizeWords += firstUpper + " "
    return capitalizeWords 


def capitalizeAll2(s):
    return " ".join([word[0].upper() + word[1:] for word in s.split(" ")])


print(capitalizeAll2("python is fun"))