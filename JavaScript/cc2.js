// Palindrome Check
// Given a string s, return true if s is a palindrome, and false otherwise.
// Ignore casing and non-alphanumeric characters.
// Example 1:
// Input: s = "refer"
// Output: true
// Example 2:
// Input: s = "racecar"
// Output: true
// Example 3:
// Input: s = “gear”
// Output: false

// SOLUTTION

// # DEFINE a function palindrome_checker passing (input_p) parameter
// # create variable palindrome_word to store the reversed string set to empty ''
// #   palindrome_word = ''
// #   use a for loop to iterate the parameter input_p
// #       use the variable palindrome_word and set to i (the elements from the iterations) + (adding elements to left) palindrome_word
// #   use if statement to compare if palindrome_word and input_p are the same by using ==
// #       if true return True
// #   else
// #       if false return False
// #
// # print and call palindrome_checker and pass word

// def palindrome_checker(input_p):
//     # return True if input_p == input_p[::-1] else False
//     palindrome_word = ''
//     for i in input_p:
//         palindrome_word = i + palindrome_word
//     if palindrome_word == input_p:
//         return True
//     else:
//         return False

// TRANSLATION
function palindromeChecker(inputP) {
    let palindromeWord = ''
    for (let i = 0; i < inputP.length; i++) {
        palindromeWord = inputP[i] + palindromeWord
    }
    if (palindromeWord.toLowerCase() === inputP.toLowerCase()) {
        return true
    } else {
        return false
    }
}

console.log(palindromeChecker('HaNnaH'))