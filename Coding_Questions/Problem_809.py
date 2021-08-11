"""Daily Coding Problem: Problem #809 [Easy]

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

given_string = ''
open_round = 0
open_curly = 0
open_square = 0

for i in given_string:
    if i == '(':
        open_round += 1
    elif i == ')':
        open_round -= 1
    elif i == '{':
        open_curly += 1
    elif i == '}':
        open_curly -=1
    elif i == '[':
        open_square += 1
    elif i == ']':
        open_square -= 1

"""
if open_round == 0 and open_curly == 0 and open_square == 0:
    print('True')
else:
    print('False')"""

bracket_1 = ''
bracket_2 = ''
if bracket_1 == '(' or ')' and open_square == 0 and open_curly == 0:
    print('False')
elif bracket_1 == '[' or ']' and open_round == 0 and open_curly == 0:
    print('False')
elif bracket_1 == '(' and bracket_2 == ')' and open_square == 0 and open_curly == 0:
    print('True')