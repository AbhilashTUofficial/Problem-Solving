# Cut the sticks
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.

### Example
`arr = [1,2,3]`

The shortest stick length is 1, so cut that length from the longer two and discard the pieces of length 1. Now the lengths are `arr = [1,2]`. Again, the shortest stick is of length 1, so cut that amount from the longer stick and discard those pieces. There is only one stick left, `arr=[1]` , so discard that stick. The number of sticks at each iteration are `answer = [3,2,1]`.

### Function Description

Complete the cutTheSticks function in the editor below. It should return an array of integers representing the number of sticks before each cut operation is performed.

cutTheSticks has the following parameter:
* int arr[n]: the lengths of each stick

### Returns
* int[]: the number of sticks after each iteration

### Input Format

The first line contains a single integer n, the size of arr.
The next line contains n space-separated integers, each an `arr[i]`, where each value represents the length of the `i'th` stick.

### Constraints
* `1 ≤ n ≤ 1000`
* `1 ≤ arr[i] ≤ 1000`

### Sample Input
    [5,4,4,2,2,8]

### Sample Output
    6
    4
    2
    1

### Explanation

|sticks lengths|length of cut|sticks cut|
|---|---|---|
|5 4 4 2 2 8|2|6|
|3 2 2 0 0 6|2|4|
|1 0 0 0 0 4|1|2|
|0 0 0 0 0 3|3|1|
|0 0 0 0 0 0|-|-|

## Answer:

[cutTheSticks](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/CutTheSticks/ANSWER/cutTheSticks.py)

