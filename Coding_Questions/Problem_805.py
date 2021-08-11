"""Daily Coding Problem: Problem #805 [Easy]

Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ...,
"ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA"."""

column = 'AB'


def column_id(column):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    column_number = 0
    for i in column:
        column_number = (column_number * 26) + (alphabet.index(i) + 1)
    return column_number

def column_name(column):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    column_number = 1
    for j in range(len(alphabet)):
        alphabet.index(j) = (column_number - 1)
    return alphabet
