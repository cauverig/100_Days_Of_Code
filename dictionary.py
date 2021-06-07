#List in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'] #a list in the dictionary
}
#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

#Nesting
people = []
person1 = {'first_name': 'Jack', 'last_name': 'Cyrus', 'age': 25, 'city': 'New York'}
people.append(person1)

person2 = {'first_name': 'Bill', 'last_name': 'Shammy', 'age': 48, 'city': 'Boston'}
people.append(person2)

person3 = {'first_name': 'Henry', 'last_name': 'Parker', 'age': 35, 'city': 'Medford'}
people.append(person3)

print(f"\nThis is a nesting example")
print(people)

for person in people[:3]:
    print(f"\nI know {person['first_name']} {person['last_name']}, who is {person['age']} years old and lives in {person['city']} city.")
