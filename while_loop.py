# while loop for pizza toppings

prompt = "\nAdd toppings: "
prompt += "\nEnter 'quit' when you are done. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Ask age and inform the price which varies as per age
ask = "\nWhat is your age? "
ask += "\nEnter 'quit' when you are done. "
state = input(ask)

while state != 'quit':
    age = int(state)

    if int(age) < 3:
        print("\nThe cost of your ticket is free")
    elif 3 <= int(age) <= 12:
        print("\nThe cost is $10")
    elif int(age) > 12:
        print("\nThe cost is $15")

    state = input(ask)