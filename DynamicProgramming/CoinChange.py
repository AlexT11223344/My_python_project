'''
Given an unlimited supply of coins of given denominations, find the minimum number of coins required to get the desired change.
'''

'''
Example: S = { 1, 3, 5, 7 }
If the desired change is 15, the minimum number of coins required is 3 
(7 + 7 + 1) or (5 + 5 + 5) or (3 + 5 + 7)
If the desired change is 18, the minimum number of coins required is 4
(7 + 7 + 3 + 1) or (5 + 5 + 5 + 3) or (7 + 5 + 5 + 1)
'''
# 1. Up to bottom (Recursive)
# x is a list represent the different coin value.
# y is a expect value.
def fun_coinChange(x, y):
    length_x = len(x)
    if y == 0:
        return 0
    elif length_x == 0:
        return 0
    for i in range(x):


    return