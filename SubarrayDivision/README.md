# Subarray Division
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
* The length of the segment matches Ron's birth month, and,
* The Sum of the integers on the squares is equal to his birth day.
  
### Example
`s = [2, 2, 1, 3, 2]`
`d = 4`
`m = 2`

Lilly wants to find segments summing to Ron's  birth day,`d = 4` with a length equalling his birth month, `m = 2`. In this case, there are two segments meeting her criteria: `[2, 2]` and `[1, 3]`.

### Function Description
birthday has the following parameters:
* int s[n]: the numbers on each of the squares of chocolate.
* int d: Ron's birth day
* int m: Ron's birth month

### Returns
* int: the number of ways the bar can be divided.

### Sample Input
    1   2   1   3   2
    3   2

### Sample Outpu
    2

## Answer:

[subarrayDivision](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/SubarrayDivision/ANSWER/subarrayDivision.py)