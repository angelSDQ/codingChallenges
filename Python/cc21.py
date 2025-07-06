# 💸 Problem: Censor Dollar Amounts (Digits Only, Preserve Commas)
# Difficulty: Medium
# Category: String Manipulation / Censorship

# 📝 Description:
# You are given a string contractText that may include monetary amounts written in USD format (e.g., $1,000,000.00).

# Your task is to censor each digit inside any dollar amount. The output must:

# Leave the dollar sign ($), commas (,), and decimal points (.) intact

# Replace every digit (0–9) within the dollar amount with an asterisk *

# Leave all non-currency parts of the string unchanged

# 🔧 Constraints:

# 1 ≤ contractText.length ≤ 2000

# Currency amounts always start with $

# A currency amount includes only digits, commas, and optionally a decimal part (e.g., .00)

# No space is present between $ and the digits

# There may be multiple currency amounts

# 🧠 Input Format:
# A single string contractText

# 🧠 Output Format:
# Return the string with each digit in a dollar amount replaced by *, keeping other characters unchanged.

# 🔍 Examples:

# Example 1:
# Input:
# "The contractor shall be paid $1,000,000.00 upon completion."
# Output:
# "The contractor shall be paid $*,***,***.** upon completion."

# Example 2:
# Input:
# "Deposit: $5000, Final: $25,000.99"
# Output:
# "Deposit: $****, Final: $**,***.**"

# Example 3:
# Input:
# "Fee: $99.95. Refund: $0.01"
# Output:
# "Fee: $**.**, Refund: $*.**"

# Example 4:
# Input:
# "No payments required."
# Output:
# "No payments required."

'''
Goals quick glance

given a string contractText
include monetary amounts (hidding the numbers)
split the string at the $ sign
only censor 0-9 and leave $ , .
'''

# Define a function hideDollarAmount() passing in 1 parameter contractText
# def hideDollarAmount(contractText):
#   declare variable
#   hiddenAmount = ""
#   findingAmount = contractText.split("$")
#   use a for loop to iterate on findingAmount
#   for amount in findingAmount:
#       hiddenNum = ""
#       firstAmount = amount[:]
#       implement an if statement to find the string that starts with the $ symbol
#       if "." in firstAmount or "," in firstAmount:
#               commas = ","
#               decimal = "."
#               hiddenNums = "*"
#       amount = amount[0] + hiddenNums + commas + decimal
#   return hiddenAmount += amount
#
# print call func


def hideDollarAmount(contractText):
    hiddenMoney = ""
    punctuationList = [".", ",", "$"]
    findingAmount = contractText.split(" ")
    # ['Deposit:', '$5000,', 'Final:', '$25,000.99'] 
    for word in findingAmount:
        if "$" in  word:
            moneyVar = ""
            for i in word:
                # print(i, "inside second for loop")
                if i in punctuationList:
                    moneyVar += i
                    print(moneyVar, "var")
                    # $5000,
                    # $25,000.99
                else:
                    moneyVar += "*"
                    print(moneyVar, "")
            word = moneyVar 
        hiddenMoney += word + " " 
    return hiddenMoney

print(hideDollarAmount("The contractor shall be paid $1,000,000.00 upon completion.")) 

