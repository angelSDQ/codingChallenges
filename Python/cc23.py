'''
"""
💵 Problem: Censor USD Money Values (No Space, Preserve Formatting)
Difficulty: Medium  
Category: String Manipulation / Censorship

📝 Description:
You're given a string `text` that may include money values strictly in **USD format with no space**, such as:
- USD1000  
- USD1,000.00  
- USD2.5M  
- USD12.35B  
- usd450K

Your task is to **censor all digits (0–9)** in these values while preserving:
- The exact prefix `USD` or `usd` (case-insensitive)
- Commas `,`
- Decimal points `.`
- Suffixes like `K`, `M`, or `B` (case-insensitive)

🧷 The match must follow this format:
• Starts with `USD` or `usd`  
• Immediately followed by a number  
• May include commas  
• May include a decimal and exactly 1–2 digits  
• May end with a valid suffix (`K`, `M`, or `B`)  

📌 Digits in all valid money values must be replaced with asterisks `*`.

⛔ Do NOT censor:
- Any number without the `USD`/`usd` prefix  
- Values with a space after `USD`  
- Values embedded in words (e.g., "USDollars")

🔧 Constraints:
• 1 ≤ text.length ≤ 2000  
• Currency values are **well-formed**  
• `USD` prefix is case-insensitive but must be **attached** to the number (no space)

🧠 Input Format:
A single string `text`

🧠 Output Format:
Return the string with all **digits (0–9) in valid USD money values** replaced by `*`.

🔍 Examples:

Example 1:  
Input:  
"The deal closed at USD1,000.00 today."  
Output:  
"The deal closed at USD*,***.** today."

Example 2:  
Input:  
"He earned USD2.5M last year."  
Output:  
"He earned USD*.*M last year."

Example 3:  
Input:  
"Invested in usd400K and withdrew USD1000000."  
Output:  
"Invested in usd***K and withdrew USD*******."

Example 4:  
Input:  
"Not valid: USD 500, USDollars, or 12345."  
Output:  
"Not valid: USD 500, USDollars, or 12345."

Example 5:  
Input:  
"Total cost is USD12,345.67 and bonus was USD25K."  
Output:  
"Total cost is USD**,***.** and bonus was USD**K."
"""
'''

'''
Goals quick glance

create a func with hideMoneyVal()
given string text
with USD values ONLY. NO spaces
ONLY censor nums 0-9
Keep original format
KEEP 'USD' or 'usd'
KEEP Commas `,` & Decimal points `.` in the same order
KEEP Suffixes like `K`, `M`, or `B` same oriiginal order
'''


# create a function hideMoneyVal() passing parameter text
# def hideMoneyVal(text):
#   create variables
#   string to hold final return set to empty string
#   hiddenAmount = ""
#   variable to hold commas and decimals in a list
#   puntuations = [",", "."]
#   list of nums
#   nums =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#   split string text to separete the sentence into list of words
#   words = text.split(" ")
#   use a for loop to iterate on the list of words
#   for word in words:
#       use an if statement to find the words with "u" or "U" at index[0] of word
#       if word[0].lower() == "u":




def hideMoneyVal(text):
    hiddenAmount = ""
    nums =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    words = text.split(" ")
    # ['Invested', 'in', 'usd400K', 'and', 'withdrew', 'USD1000000.']
    for word in words:
        if word[:3].lower() == "usd":
            hideNums = ""
            print(hideNums, "test")
            for i in range(len(word)):
                if word[i] not in nums:
                    hideNums += word[i]
                else:
                    hideNums += "*"
            word = hideNums
        hiddenAmount += word + " "
    return hiddenAmount

print(hideMoneyVal("Total cost is USD12,345.67 and bonus was USD25K."))