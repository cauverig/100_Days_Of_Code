"""Daily Coding Problem: Problem #825 [Easy]


Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81]"""


given_list = [-9, -2, 0, 2, 3]
new_list = []
for i in given_list:
    new_list.append(i**2)

new_list.sort()
print(new_list)



