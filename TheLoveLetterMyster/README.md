# The Love Letter Mystery
James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

1. He can only reduce the value of a letter by 1, i.e. he can change `d` to `c`, but he cannot change `c` to `d` or `d` to `b`.
2. The letter `a` may not be reduced any further.

Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

### Example
`s = cde`

The following two operations are performed: cde → cdd → cdc. Return 2

### Function Description

theLoveLetterMystery has the following parameter:
* string s: the text of the letters.

### Return
* int: the minimum number of operations

### Constraints

`1 ≤ q ≤ 10`

All string are composed of lower case English letters.

### Sample Input
    abc
    abcba
    abcd
    cba

### Sample Output
    2
    0
    4
    2

### Explanation

1. abc : abc → abb → aba : return 2
2. abcba : already a palindrome : return 0
3. abcd : abcd → abcc → abcb → abbb → abba: return 4
4. cba : cba → bba → aba : return 2

## Answer:

[theLoveLetterMystery](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/TheLoveLetterMystery/ANSWER/theLoveLetterMystery.py)

