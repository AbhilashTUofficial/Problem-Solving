# Repeated String
There is a string s, of lowercase English letters that is repeated infinitely many times. Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

### Example
`s = 'abcac'`,
`n = 10`

The substring we consider is `abcacabcac`, the first 10 characters of the infinite string. There are 4 occurrences of a in the substring.

### Function Description
repeatedString has the following parameters:
* s: a string to repeat
* n: the number of characters to consider

### Return
* int: the frequency of a in the substring

### Sample Input
    aba
    10

### Sample Output
    7

### Explanation
The first `n = 10` letters of the infinite string are abaabaabaa. Because there are 7 a's, return 7.

## Answer:

[repeatedString](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/RepeatedString/ANSWER/repeatedString.py)