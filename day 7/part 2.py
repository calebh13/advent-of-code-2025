# INPUT_FILE = r"day 7/test.txt"
INPUT_FILE = r"day 7/input.txt"

# The only change we'll make to this is keeping track of the number of timelines in each grid position
# Then we just sum up the bottom row at the end

if __name__ == "__main__":
    lines = []
    with open(INPUT_FILE, "r") as file:
        for line in file:
            lines.append([c for c in line]) # essentially, make the characters mutable

    lines[1][lines[0].index("S")] = 1 # make initial beam below source
    for row in range(1, len(lines) - 1):
        for col in range(len(lines[row])):
            if isinstance(lines[row][col], int):
                val = int(lines[row][col])
                if lines[row + 1][col] == '^':
                    # These may overwrite each other, but this means we never count duplicates
                    left = lines[row + 1][col - 1]
                    right = lines[row + 1][col + 1]
                    lines[row + 1][col - 1] = left + val if isinstance(left, int) else val
                    lines[row + 1][col + 1] = right + val if isinstance(right, int) else val
                else:
                    lower = lines[row + 1][col]
                    lines[row + 1][col] = lower + val if isinstance(lower, int) else val
                    
    print(sum([n for n in lines[-1] if isinstance(n, int)]))
