# Permuting Two Arrays
There are two n-element arrays of integers, A and B. Permute them into some A' and B' such that the relation `A'[i] + B'[i] ≥ k` holds for all i where `0 ≤ i ≤ n`.
There will be q queries consisting of A,B and k. For each query, return YES if some permutation A',B' satisfying the relation exists. Otherwise, return NO.

### Example
`A = [0,1]`, `B = [0,2]`, `k = 1`

A valid A' ,B' is `A' = [1,0]` and `B' = [0,2]` : `1 + 0 ≥ 1` and `0 + 2 ≥ 1`. Return YES.

### Function Description
twoArrays has the following parameters:
* int k: an integer
* int A[n]: an array of integers
* int B[n]: an array of integers

### Returns
* string: either YES or NO

### Sample Input
    A = [2,1,3], B = [7,8,9]
    A = [1,2,2,1], B = [3,3,3,4]

### Sample Output
    YES
    NO

### Explanation

`A = [2,1,3]`, `B = [7,8,9]`, `k = 10`
i.e,
`A' = [1,2,3]`, `B' = [9,8,7]`
0. `A[0] + B[0] = 1 + 9 = 10 ≥ k`
1. `A[1] + B[1] = 2 + 8 = 10 ≥ k`
2. `A[2] + B[2] = 3 + 7 = 10 ≥ k`
So, return YES

`A = [1,2,2,1]`, `B = [3,3,3,4]`, `k = 5`
i.e,
`A' = [1,1,2,2]`, `B' = [4,3,3,3]`
0. `A[0] + B[0] = 1 + 4 = 5 ≥ k`
1. `A[1] + B[1] = 1 + 3 = 4 < k`
2. `A[2] + B[2] = 2 + 3 = 5 ≥ k`
3. `A[3] + B[3] = 2 + 3 = 5 ≥ k`

So, return NO

## Answer:

[permutingTwoArrays](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/PermutingTwoArrays/ANSWER/permutingTwoArrays.py)