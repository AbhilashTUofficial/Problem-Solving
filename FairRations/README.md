# Fair Rations
You are the benevolent ruler of a castle, and today you're distributing bread. Your subjects are in a line, and some of them already have some loaves. Times are hard and your castle's food stocks are dwindling, so you must distribute as few loaves as possible according to the following rules:
1. Every time you give a loaf of bread to some person i, you must also give a loaf of bread to the person immediately in front of or behind them in the line `(i.e, i+1 or i-1)`.
2. After all the bread is distributed, each person must have an even number of loaves.

Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute to satisfy the two rules above. If this is not possible, Print NO.

### Example
`B = [4,5,6,7]`
* We can first give a loaf to `i = 3 and i = 4 so B = [4,5,7,8]`
* Next we give a loaf to `i = 2 and i = 3 and have B = [4,6,8,8]` which satisfies our conditions.
  
All of the counts are now even numbers. We had to distribute 4 loaves.

### Function Description
fairRation has the following parameter:
* int B[n]: the numbers of loaves each persons starts with.

### Returns
* string: the minimum number of loaves required, cast as a string, or 'NO'.

### Constraints
* 1 ≤ b[i] ≤ 10
  
### Sample Input
    [2, 3, 4, 5, 6]
    [1, 2]

### Sample Output
    4
    NO

## Answer:

[fairRations](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/FairRations/ANSWER/fairRations.py)

