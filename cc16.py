'''
Problem: Mask Phone Number Digits (Asterisk Only)
Difficulty: Easy
Category: String Manipulation / Masking

📝 Description:
Given a phone number string phone, return a new string where every digit is replaced with an asterisk (*), except for the last 4 digits.

Non-digit characters (such as -, (, ), or space) must remain unchanged and in their original positions.

The last 4 characters of the string are guaranteed to be digits and must be left unmasked.

🔧 Constraints:
5 <= phone.length <= 100

The string contains only:

Digits '0'–'9'

Formatting characters: -, (, ), and space

The last 4 characters of phone are digits

The string contains at least 4 digits

🧠 Input Format:
A single string phone

🧠 Output Format:
Return a masked string where only the last 4 digits are shown, and all earlier digits are replaced by *. Formatting characters remain unchanged.

🔍 Examples:
Example 1:
Input:
"123-456-7890"
Output:
"***-***-7890"

Example 2:
Input:
"(123) 456 7890"
Output:
"(*) * 7890"

Example 3:
Input:
"9876543210"
Output:
"******3210"

Example 4:
Input:
"1234"
Output:
"1234"
(Only 4 digits — none are masked)

Example 5:
Input:
"***-***-1234"
Output:
"***-***-1234"
(Already masked correctly)
'''


# Define a function maskingPhoneNumber() passing one parameter string phone
# def maskingPhoneNumber(phone):
#   define 3 variables
#   maskedPhoneNumber = ""
#   hidddenNumbers = ""
#   unMaskedNumbers = "" 
#   use an if statement and len to count the elements
#   if len(phone) <= 4:
#       return phone
#   elif the length is greater than 4 slice phone string
#   elif len(phone) > 4:
#       store the last 4 unchanged numbers to unMaskedNumbers and the rest to hidddenNumbers using slice
#       unMaskedNumbers = phone[-4:]
#       hidddenNumbers = phone[:-4]
#   use a for loop on hidddenNumbers
#   for i in hidddenNumbers:
#       use an if statement to locate the occurances of the special characters
#       if i not in unchangedCharacter:
#           maskedPhoneNumber += "*"
#       else:
#           maskedPhoneNumber += i
#       return maskedPhoneNumber + unMaskedNumbers
#
# print and call function

def maskingPhoneNumber(phone):
    maskedPhoneNumber = ""
    unMaskedNumbers = ""
    hidddenNumbers = ""
    unchangedCharacter = ["-", "(", ")", " "]
    if len(phone) <= 4:
        return phone
    elif len(phone) > 4:
        unMaskedNumbers = phone[-4:]
        print(unMaskedNumbers)
        hidddenNumbers = phone[:-4]
        print(hidddenNumbers)
    # "(757)-955"
    # "(***)-***"
    for i in hidddenNumbers:
        if i not in unchangedCharacter:
            maskedPhoneNumber += "*"
        else:
            maskedPhoneNumber += i
    return maskedPhoneNumber + unMaskedNumbers

print(maskingPhoneNumber("(757) 955 7890"))