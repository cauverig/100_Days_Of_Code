prompt = "What is your age? "
prompt += "\nEnter quit when done. "
word = input(prompt)

while word != 'quit':
    age = int(word)

    if int(age) > 100:
        print("invalid input")

    word = input(prompt)