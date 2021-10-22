# Funny String
In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. abc -> cba . Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

### Example
`s = 'lmnop'`

The ordinal values of the charcters are `[108,109,110,111,112]` `reversed(s) 'ponml'` and the ordinals are `[112,111,110,109,108]`. The absolute differences of the adjacent elements for both strings are `[1,1,1,1]`, so the answer is Funny.

### Function Description
funnyString has the following parameter:
* string s:a string to test

### Returns
* string: either Funny or Not Funny

### Input Format
The  first line contains an integer q, the number of queries.
The next q lines each contain a string s.

### Constraints
* `1 ≤ q ≤ 10`
* `2 ≤ len(s) ≤ 10000`

### Sample Input
    acxz
    bcxz

### Sample Output
    Funny
    Not Funny

### Explanation
Let r be the reverse of s.

`s = 'acxz', r = 'zxca'`
Corresponding ASCII values of characters of the strings:
`s = [97,99,120,122] and r = [122,120,99,97]`
For both strings the adjacent difference list is `[2,21,2]`.

`s = 'bcxz', r = 'zxcb'`
Corresponding ASCII values of characters of the strings:
`s = [98,99,120,122] and r = [122,120,99,98]`
s adjacent difference is `[1,21,2]`, r adjacent difference is `[2,21,1]`.

## Answer:

[funnyString](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/FunnyString/ANSWER/funnyString.py)

