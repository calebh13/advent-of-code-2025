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
            password += (turns // 100)
            turns %= 100
            # Make sure NOT to count starting on 0 as a crossing!
            if dial != 0 and dial - turns <= 0:
                password += 1
            dial -= turns 
        else:
            # If dial is at 50, and we do R1000 (giving 1050), we pass through zero 10 times
            dial += turns
            password += dial // 100
        dial %= 100

        print(f"Dial: {dial}, password: {password}")

print(password)
