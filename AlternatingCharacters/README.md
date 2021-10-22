# Alternating Characters
You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

### Example
`s = AABAAB`

Remove an A at positions 0 and 3 to make `s = ABAB` in 2 deletions

### Function Description

alternationgCharacters has the following parameters:
* string s: a string

### Returns
* int: the minimum number of deletions required.

### Input Format
The first line contains an integer q, the number of queries.
The next q lines each contain a string s to analyse.

Contraints
* `1 ≤ q ≤ 10`
* `1 ≤ len(s) ≤ 10^5`
* Each string s will consist only of characters A and B.

### Sample Input

    AAAA
    BBBBB
    ABABABAB
    BABABA
    AAABBB

### Sample Output
    3
    4
    0
    0
    4


## Answer:

[alternatingCharacters](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/AlternatingCharacters/ANSWER/alternatingCharacters.py)
