'''
Problem: Smart Email Masking (Strict Privacy Version)
Difficulty: Medium
Category: String Manipulation / Masking

📝 Description:
Given an email address string email, return a new string where the username part (before the @) is masked as follows:

If the username length is greater than 2:

Keep the first and last character of the username

Replace all other characters with asterisks *

If the username length is 2 or less, replace all characters in the username with asterisks

The domain (everything after the @) must remain unchanged.

🔧 Constraints:

3 ≤ email.length ≤ 100

The email contains exactly one @

The username and domain contain only:

lowercase/uppercase English letters

digits

underscores _, hyphens -, or periods .

The username is at least 1 character

🧠 Input Format:
A single string email

🧠 Output Format:
Return the masked email string

🔍 Examples:

Example 1:
Input:
"john.doe@example.com"
Output:
"j******e@example.com"

Example 2:
Input:
"a@example.com"
Output:
"*@example.com"
(Username has 1 character — fully masked)

Example 3:
Input:
"ab@example.com"
Output:
"**@example.com"
(Username has 2 characters — fully masked)

Example 4:
Input:
"alex_92@domain.net"
Output:
"a*****2@domain.net"
'''

"""
Goal Quick Glance

- passing 1 parameter email
- return new string
    where the username part (before the @) is masked
- Replace characters with asterisks *
- if the lenght > 2 
    Keep the first and last character
- if the length <= 2
    Replace all characters with asterisks *

"""

# define parameter maskingEmailUser() passing 1 parameter (email)
# def maskingEmailUser(email):
#   declare variables
#   emailUser = email.split("@")[0]
#   endOfDomain = email.split("@")[1]
#   maskedUser = ""
#   use if statement to check the length of email
#   if len(email) <= 2:
#       use for loop to iterate to find the length pf string email
#       for i in email:
#          maskedUser += "*"
#          return maskedUser + "@" + endOfDomain
#   use elif to check if the length of the email is > 2
#   elif len(emailUser) > 2:


def maskingEmailUser(email):
    emailUser = email.split("@")[0]
    endOfDomain = email.split("@")[1]
    maskedUser = ""
    firstUser = ""
    lastUser = ""
    hiddenUser = ""
    if len(emailUser) <= 2:
        for i in emailUser:
            maskedUser += "*"
        return maskedUser + "@" + endOfDomain
    elif len(emailUser) > 2:
        firstUser = emailUser[:1]
        lastUser = emailUser[-1:]
        hiddenUser = emailUser[1:-1]
    return firstUser + len(hiddenUser[1:-1]) * "*" + lastUser + "@" + endOfDomain

# def maskingEmailUser(email):
#     emailUser, endOfDomain = email.split("@")
#     return (emailUser[0] + (len(emailUser[1:-1]) * "*" + emailUser[-1]) if len(emailUser) > 2 else (len(emailUser) * "*")) + "@" + endOfDomain

print(maskingEmailUser("ye@example.com"))