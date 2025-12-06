# now we need to find invalid IDs that have something repeated AT LEAST twice.
# however, they can *only* be made with repetition: that is, 11114 is NOT invalid; it must be something like 121212.
# this gets extraordinarily complicated if you do it the same way i did part 1: you have weird divisor stuff, prime checking,
# all sorts of strangeness. instead i just bruteforced it with regex, since the intervals aren't all that big :)

import re

# ^ forces the regex to match at the start of the string
# (.+) captures any character with '.' and repeats it 1 or more times with '+'. This is the bulk of the logic
# \1+ refers to the captured text with '\1' and repeats THAT 1 or more times
# $ forces the regex to match at the end of the string.
# So this regex must match the entire string, and it has to consist of 1 or more characters repeated 1 or more times.
# We can just loop through all numbers in the intervals from here!

REGEX = r"^(.+)\1+$"

# INPUT_FILE = r"day 2/test.txt"
INPUT_FILE = r"day 2/input.txt"

if __name__ == "__main__":
    idSum = 0
    pattern = re.compile(REGEX)
    with open(INPUT_FILE, "r") as file:
        line = file.readline()
        intervals = [[int(num) for num in interval.split("-")] for interval in line.split(",")]
        for interval in intervals:
            for id in range(interval[0], interval[1] + 1):
                if bool(pattern.match(str(id))):
                    idSum += id
                    print(f"Invalid ID: {id}")
            
    print(idSum)
