# In Python, (0 - 1) % 100 == 99. So negative modulo works the same as the dial.
# (in C, -1 % 100 == -1.)
INPUT_FILE = r"day 1/input.txt"

# Password is number of times that the dial lands on 0, and it starts at 50
password = 0
dial = 50

with open(INPUT_FILE, 'r') as file:
    for line in file:
        dir = line[0]
        turns = int(line[1:])
        if dir == 'L':
            turns *= -1
        dial = (dial + turns) % 100
        if dial == 0:
            password += 1
        #print(f"Dial: {dial}")

print(password)
