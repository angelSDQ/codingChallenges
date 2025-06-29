'''
Problem: Hide Email Domain
Difficulty: Easy
Category: String Manipulation / Masking

📝 Description:
You are given a valid email address string email. Your task is to return a new string where the domain part (everything after the @ symbol) is replaced with asterisks *, but keeping the @ symbol and the domain extension (such as .com, .org, .net, etc.) intact.

The username part (before the @) must remain unchanged.

🔧 Constraints:

email.length is between 5 and 100 characters.

email is a valid email address of the form: username@domain.extension.

The domain part (between @ and the last .) may include letters, digits, hyphens -, and periods .

The domain extension (after the last .) is at least 2 and at most 5 lowercase letters.

🧠 Input Format:
A single string email

🧠 Output Format:
Return a masked version of the email where the domain is replaced by asterisks (same number of characters), but the username and extension remain visible.

🔍 Examples:

Example 1:
Input:
"john.doe@example.com"
Output:
"john.doe@*******.com"

Example 2:
Input:
"school.edu"
Output:
"alice@******.edu"

Example 3:
Input:
"x@a.io"
Output:
"x@*.io"

Example 4:
Input:
"user123@my-domain.org"
Output:
"user123@***********.org"
'''

'''
Goals quick glance

- email string to pass
- return new string
- everything after the @ replaced with "*" 



'''
# emailTest = "alice@school.edu"
# print(emailTest.split("@")[1].split(".")[1])

# Define a function maskingEmail() passing in 1 parameter email
# def maskingEmail(email):
#   declare variables
#   use .split() method to separate email at the @ and store to emailName
#   emailName = email.split("@")[1]
#   endOfEmail = ""
#   
#   


def maskingEmail(email):
    emailName = email.split("@")[0]
    endOfEmail = email.split("@")[1]
    secretDomain = ""
    print(emailName, "test")
    print(endOfEmail, "test 2")
    for i in range(len(endOfEmail)):
        if endOfEmail[i] == ".":
            secretDomain += "*"
            return emailName + "@" + secretDomain + endOfEmail[i:]
        secretDomain += "*"

print(maskingEmail("john.doe@example.com"))