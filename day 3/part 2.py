# INPUT_FILE = r"day 3/test.txt"
INPUT_FILE = r"day 3/input.txt"
NUM_CHOICES = 12

# We now have to turn on 12 batteries rather than just 2, which gives 100c12 ~= 1 quadrillion valid choices instead of 2^15;
# this is a combinatorial explosion. how can we do it? let's study an example of 7 choose 3.

# say the bank is 6735421. clearly, the max is 754. how do we get there?
# start off with everything set to 0, and we need to choose the first number.

# the first number is ALWAYS the max number in the length range(0, len(line) - numChoicesLeft).
# i.e., scan the string "67354" for its max, and set num[0] to the max (7).
# then, your search begins at the next position, pos 2. we have 2 choices left, so next search is:

# scan "3542" for its max. set num[1] to its max, 5. start next search at position 4.

# we have 1 choice left, so scan "421" for its max. now since we've scanned the whole string, we're done.

# this naturally extends to longer banks and # of battery choices.


if __name__ == "__main__":
    joltageSum = 0
    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            nums = [0] * NUM_CHOICES
            pos = 0
            for numIdx, _ in enumerate(nums):
                maxNum, maxPos = 0, 0
                choicesLeft = NUM_CHOICES - (numIdx)
                substring = line[pos:len(line) - choicesLeft + 1]
                for i in range(pos, len(line) - choicesLeft + 1):
                    if int(line[i]) > maxNum:
                        maxNum = int(line[i])
                        maxPos = i
                nums[numIdx] = maxNum
                pos = maxPos + 1 # start at the next number
            joltage = int("".join(map(str, nums)))
            print(f"Joltage: {joltage}")
            joltageSum += joltage
        print(joltageSum)
