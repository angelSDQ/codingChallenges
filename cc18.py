'''
👤 Problem: Mask Username (Asterisk All But First and Last)
Difficulty: Easy
Category: String Manipulation / Masking

📝 Description:
Given a username string username, return a new string where all characters except the first and last are replaced with asterisks *.

If the length of the username is 2 or fewer, return the string unchanged.

🔧 Constraints:

1 ≤ username.length ≤ 100

The username contains only lowercase and uppercase English letters, digits, and underscores (_)

🧠 Input Format:
A single string username

🧠 Output Format:
Return the masked username where only the first and last characters are visible, and the rest are replaced with *. If the username has 2 or fewer characters, return it as-is.

🔍 Examples:

Example 1:
Input:
"johndoe"
Output:
"j*****e"

Example 2:
Input:
"a1b2c3d4"
Output:
"a******4"

Example 3:
Input:
"xy"
Output:
"xy"
(Only 2 characters — nothing is masked)

Example 4:
Input:
"Z"
Output:
"Z"

Example 5:
Input:
"user_name_123"
Output:
"u***********3"
'''

'''
Goals quick glance

- username string 
- return a new string 
- new string maskes all characters exept the first and last with an *
- if username is 2 or less return unchanged
'''

# define a function secretUsername() passing one parameter username
# def secretUsername(username):
#   declare 3 variables
#   maskedUsername = ""
#   firstUnmaskedChar = ""
#   masked = ""
#   use if statement to check the length of the username
#   if len(username) <= 2:
#       if less than 2 return it
#       return username
#   use elif to slice username string if greater than 2
#   elif len(username) > 2:
#       store 1st unchanged charter to firstUnmaskedChar by using slice username[:1]
#       firstUnmaskedChar = username[:1]
#       store last unchanged charter to lastUnmaskedChar by using slice username[-1:]
#       lastUnmaskedChar = username[-1:]
#       store the characters in between in secretUser
#       secretUser = username[1:-1]
#   use a for loop to iterate on secretUser
#   for i in secretUser:
#       set the i to * and store to maskedUsername
#       maskedUsername += "*"
#   return firstUnmaskedChar + maskedUsername + lastUnmaskedChar
#
# print call function




def secretUsername(username):
    maskedUsername = ""
    firstUnmaskedChar = ""
    lastUnmaskedChar = ""
    secretUser = ""
    if len(username) <= 2:
        return username
    elif len(username) > 2:
        firstUnmaskedChar = username[:1]
        lastUnmaskedChar = username[-1:]
        secretUser = username[1:-1]
    for i in secretUser:
        maskedUsername += "*"
    return firstUnmaskedChar + maskedUsername + lastUnmaskedChar

# def secretUsername2(username):
#     return username[0] + (len(username[1:-1]) * "*") + username[-1] if len(username) > 2 else username 

print(secretUsername("user_name_123"))