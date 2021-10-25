# Electronics Shop
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

### Example
`b = 60`,
`keyboards = [40,50,60]`,
`drives = [5,8,12]`

The person can buy a 40 keyboard + 12 drive = 52, or a 50 keyboard + 8 drive = 58. Choose the latter as the more expensive option and return 58.

### Function Description
getMoneySpent has the following parameters:
* int keyboards[n]: the keyboard prices
* int drives[m]: the drive prices
* int b: the budget

### Return
* int: the maximum that can be spent, or -1 if it is not possible to buy both items.

### Sample Input
    3 1
    5 2 8
    10

### Sample Output
    9

## Answer:

[electronicsShop.py](https://github.com/AbhilashTUofficial/Problem-Solving/blob/master/ElectronicsShop/ANSWER/electronicsShop.py)