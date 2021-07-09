from random import randint #randint to randomly pick a number
trials = 100000
success = 0

# repeated random sampling

for trial in range(trials):
    faces = set()
for rolls in range(6):
    roll = randint(1, 6)
    faces.add(roll)
if len(faces) == 6:
    success += 1

print("probability of success = {}".format(success/trials))
