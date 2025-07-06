'''
📵 Problem: Censor Phone Numbers (No Spaces, Preserve Formatting)
Difficulty: Medium
Category: String Manipulation / Censorship

⸻

📝 Description:
You are given a string text that may contain U.S.-style phone numbers written without spaces (e.g., 123-456-7890, (123)456-7890, +1(123)456-7890, etc.).

Your task is to censor each digit (0–9) within any phone number, while preserving all formatting characters such as parentheses (), dashes -, dots ., and the optional country code +1.

🔒 Replace all digits in phone numbers with asterisks *.
✔ Leave non-digit formatting and all other non-phone-number content unchanged.

⸻

🔧 Constraints:
	•	1 ≤ text.length ≤ 2000
	•	Phone numbers always contain exactly 10 digits, optionally preceded by a U.S. country code (+1)
	•	Valid phone number formats (without any spaces) include:
	•	123-456-7890
	•	(123)456-7890
	•	123.456.7890
	•	1234567890
	•	+1(123)456-7890
	•	Phone numbers are properly formatted and not embedded in other alphanumeric sequences

⸻

🧠 Input Format:
A single string text

🧠 Output Format:
Return the string with all digits in phone numbers replaced by *, formatting intact.

⸻

🔍 Examples:

Example 1:
Input:
"Call (123)456-7890 immediately."
Output:
"Call (***)***-**** immediately."

Example 2:
Input:
"Office: 123.456.7890, Cell: 1234567890"
Output:
"Office: ***.***.****, Cell: **********"

Example 3:
Input:
"Alternate: +1(555)123-4567"
Output:
"Alternate: +1(***)***-****"

Example 4:
Input:
"Nothing to censor here."
Output:
"Nothing to censor here."
'''


'''
create a def
create variables
text.split(" ")
for word[0] in punctualita
if ( ) num +
'''


def maskTheNumbers(text):
    hiddenNumber = ""
    numsAndCharacters = ["(", ")", "+", "1"]
    nums =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    words = text.split(" ")
    for word in words:
        if word[0] in numsAndCharacters:
            secretNum = ""
            for i in range(1, len(word)):
                if word[i] not in nums:
                    secretNum += word[i]
                elif word[i] in nums and word[i-1] == "+":
                    secretNum += "+1"
                else:
                    secretNum += "*"
            word = secretNum
        hiddenNumber += word + " "
    return hiddenNumber

print(maskTheNumbers("Alternate: +1(555)123-4567"))