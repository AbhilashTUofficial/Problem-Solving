# Marc's Cakewalk
Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least `2^j x c` miles to maintain his weight.

### Example
`calorie = [5,10,7]`

If he eats the cupcakes in the order shown, the miles he will need to walk are `(2^0 x 5)+(2^1 x 10)+(2^2 x 7) = 53`. This is not the minimum, though, so we need to test other orders of consumption. In this case, our minimum miles in calculated as `(2^0 x 10)+(2^1 x 7)+(2^2 x 5) = 10 + 14 + 20 = 44`. 
Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.

### Function Description
marcsCakeWalk has the following parameter:
* int calories[n]: the calorie counts for each cupcake

### Returns
* long: the minimum miles necessary

### Constraints
* `1 ≤ n ≤ 40`

### Sample Input
    1 3 2

### Sample Output
    11


## Answer:

[marc'sCakewalk](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/Marc'sCakewalk/ANSWER/marc'sCakewalk.py)