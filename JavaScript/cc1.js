// Reverse String
// Given a string s, return the string reversed.
// You must build the reversed string without using the built-in reverse() method.
// Example 1:
// Input: s = "hello"
// Output: "olleh"
// Example 2:
// Input: s = "ChatGPT"
// Output: "TPGtahC"

// #print('hello world')

// DEFINE a function reversed_string passing (input_s) parameter
// create variable reversed_s to store the reversed string set to empty ''
//    reversed_s = ''
//    use a for loop to iterate the parameter input_s
//        use the variable reversed_s and set to i (the elements from the iterations) + (adding elements to left) reversed_s
//    return reversed_s
//
// print and call function


// def reversed_string(input_s):
//     reversed_s = ''
//     for i in input_s:
//         reversed_s = i + reversed_s    
//     return reversed_s

// TRANSLATION
function reversedString(inputS) {
    let reversedS = ''
    for (let i = 0; i < inputS.length; i++) {
        reversedS = inputS[i] + reversedS;
    }
    return reversedS;
}

console.log(reversedString('ChatGPT'))