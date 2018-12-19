# Exercise 1
lyst = list()

with open("coordinates.py", "r") as f:
    lyst.append(f.read())

for line in lyst:
    print(line)


# Exercise 2
answer = input("How many licks does it take to get to the center of a Tootsie Pop?")

with open("answer.txt", "w") as f:
    f.write(answer)


with open("answer.txt", "r") as f:
    answer = f.read()
    print(answer)

