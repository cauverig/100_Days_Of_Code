"""Daily Coding Problem: Problem #819 [Easy]

Given a array of numbers representing the stock prices of a company in chronological order,
 write a function that calculates the maximum profit you could have made from buying and selling that stock once.
 You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
 since you could buy the stock at 5 dollars and sell it at 10 dollars."""

given_list = [9,11,8,5,7,10]
profit_list = []

for i in range(len(given_list)):
    for j in range(i+1, len(given_list)):
        profit = given_list[j] - given_list[i]
        profit_list.append(profit)

print(max(profit_list))



