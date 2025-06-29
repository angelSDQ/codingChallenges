# Problem: Mask Email Username (Asterisk Only)

# Difficulty: Easy
# Category: String Manipulation / Masking

# Description:

# Given an email address string email, return a new string where the entire username (the part before the '@' symbol) is replaced with asterisks '*'. The domain part of the email (the part after the '@') should remain unchanged.

# Examples:

# Input: "john.doe@example.com"
# Output: "****@example.com"

# Input: "j@example.com"
# Output: "*@example.com"

# Input: "jo@example.com"
# Output: "**@example.com"

# Input: "johndoe@example.com"
# Output: "****@example.com"

# Constraints:

# •    1 <= len(email) <= 100
# •    email contains one '@' character.
# •    The username and domain contain only alphanumeric characters and the following symbols: . _ - +


# define a function maskingEmail() pass one parameter string email
# def maskingEmail(email):
#   declare 3 varibles and set to empty string
#   securedEmail = ""
#   unMaskedEmail = ""
#   maskedEmail = ""
#   use a for loop to iterate through email using range and len to get the index
#   for i in range(len(email)):
#       use if statemnet to find what the index of @ symbol is
#       if email[i] == "@":
#           store value of index number to inxNum
#           inxNum = i
#           use inx to slice the variables before and after the @ symbol
#           unMaskedEmail = email[-inxNum:]  // elements after @
#           maskedEmail = email[:-inxNum]    // elements before @
#    use for loop to iterate maskedEmail and change these to "*" by storing in secureEmail
#    for i in maskedEmail:
#           securedEmail += "*"
#    return and concatenate to bring everything togeteher
#    return securedEmail + unMaskedEmail
#
#
#  print and call
#  print(maskingEmail("email"))        

def maskingEmail(email):
    securedEmail = ""
    for i in range(len(email)):
        if email[i] == "@":
            return securedEmail + email[i:]
        securedEmail += "*"

print(maskingEmail("angel@gmail.com"))