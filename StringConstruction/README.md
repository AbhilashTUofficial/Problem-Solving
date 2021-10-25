# Sring Construction
Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations with the given costs. She can perform them any number of times to construct a new string p:

* Append a character to the end of string p at a cost of 1 dollar.
* Choose any substring of p and append it to the end of p at no charge.

Given n strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.

### Example
`s = 'abcabc'

It can be copied for 3 dollars, start by copying a,b and c individually at a cost of 1 dollar per character. String p = abc at this time. Copy p[0:2] to the end of p at no cost to complete the copy.

### Function Description

stringConstruction has the following parameter:

* s: a string

### Output Format
For each string s[i] print the minimum cost of constructing a new string p[i] on a new line.

### Sample Input
    abcd
    abab
### Sample Output
    4
    2

### Explanation

`s = 'abcd'`

0. `s = 'abcd'` : `p = ''`
1. `s = 'abcd'` → `'a'` : `p = 'a'` 
2. `s = 'bcd'`  → `'b'` : `p = 'ab'` 
3. `s = 'cd'`   → `'c'` : `p = 'abc'` 
4. `s = 'd'`    → `'d'` : `p = 'abcd'` 

Return 4

`s = 'abab'`

0. `s = 'abab'` : `p = ''`
1. `s = 'abab'` → `'a'` : `p = 'a'` 
2. `s = 'bab'`  → `'b'` : `p = 'ab'` 
3. `s = 'ab'`   → `'ab'` : `p = 'abab'` 

Return 2

## Answer:

[stringConstruction](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/StringConstruction/ANSWER/stringConstruction.py)
