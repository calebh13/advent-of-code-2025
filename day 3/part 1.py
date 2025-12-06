# INPUT_FILE = r"day 3/test.txt"
INPUT_FILE = r"day 3/input.txt"

# Example line is 811111111111119
# This is kind of like Best Time to Buy and Sell Stock; the higher digit must be to the left of the lower, and we cannot change the ordering.

# I think the key insight is that any time we reach number > left digit, we should automatically left digit to it
# (as long as we have another digit remaining in the line).
# Since the upper digit is 10x more important than the right, a greedy approach for it will ALWAYS produce the highest left digit.

# Basically:
# 1. Set left, right = 0, 0. Loop through the line (for i in range(0, len(line) - 1) so we always have a right num).
# 2. If line[i] > left, set left = line[i], right = line[i+1] (to enforce ordering).
# 3. If line[i] > right, set right = line[i].
# 4. Return left * 10 + right.

if __name__ == "__main__":
    joltageSum = 0
    with open(INPUT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            left, right = 0, 0
            for i in range(0, len(line) - 1):
                if int(line[i]) > left:
                    left = int(line[i])
                    right = int(line[i + 1]) # enforce proper ordering
                elif int(line[i]) > right:
                    right = int(line[i])

            # We need to check the last number manually, since our loop skips it
            lastNum = int(line[len(line) - 1])
            right = lastNum if lastNum > right else right

            joltage = left * 10 + right
            print(f"Joltage: {joltage}")
            joltageSum += joltage
        print(joltageSum)
