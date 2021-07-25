
"""Daily Coding Problem: Problem #821 [Easy]

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements,
 return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False."""


given_list = [-6, 0, 2, 40]

def func(gin_list):
    for i in range(len(gin_list)):
        if i == gin_list[i]:
            return i

    return 'False'

print(func(given_list))

# check if the value of the element matches the index