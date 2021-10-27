# Minimum Distances
The distance between two array values is the number of indices between them. Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, return -1.

### Example
`a = [3,2,1,2,3]`,
There are two matching pairs of values: 3 and 2. The indices of the 3's are `i = 0 and j = 4`, so their distance is `d[i,j] = |j - i| = 4`. The indices of the 2's are `i = 1 and j = 3`, so their distance is `d[i,j] = |j - i| = 2`. The minimum distance is 2.

### Function Description
minimumDistances has the following parameter:
* int a[n]: an array of integers

### Return
* int: the minimum distance found or -1 if there are no matching elements.

### Sample Input
    [7, 1, 3, 4, 1, 7]

### Sample Output
    3

## Answer:

[minimumDistances](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/MinimumDistances/ANSWER/minimumDistances.py)