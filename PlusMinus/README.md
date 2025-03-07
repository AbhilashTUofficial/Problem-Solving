# Plus Minus
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with `6` places after the decimal.

### Example
`arr = [1, 1, 0, -1, -1]`
There are `n = 5` elements, two positivfe, two negative and one zero. Their ratios are `2/5 = 0.400000, 2/5 = 0.400000` and `1/5 = 0.200000`. Results are printed as:
    0.400000
    0.400000
    0.200000

### Function Description 
Complete the plusMinus function.
plusMinus has the following parameter:
* int `arr[n]`: an array of integers.

### Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

### Input Format
The first line contains an integer, `n`, the size of the array.
The second line contains `n` space-separated integers that describe `arr[n]`.

### Constraints
`0 < n ≤ 100 `
`-100 ≤ arr[i] ≤ 100`

### Output Format
Print the following 3 lines, each to 6 decimals:

- proportion of positive values
- proportion of negative values
- proportion of zeros

### Sample Input
    -4  3   -9  0   4   1

### Sample Output
    0.500000
    0.333333
    0.166667

### Explanation
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: `3/6 = 0.500000`, negative: `2/6 = 0.33333` and zeros: `1/6 = 0.166667`.

## Answer:

[plusMinus](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/PlusMinus/ANSWER/plusMinus.py)