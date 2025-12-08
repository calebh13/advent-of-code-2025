INPUT_FILE = r"day 7/test.txt"
INPUT_FILE = r"day 7/input.txt"

if __name__ == "__main__":
    lines = []
    with open(INPUT_FILE, "r") as file:
        for line in file:
            lines.append([c for c in line]) # essentially, make the characters mutable

    lines[1][lines[0].index("S")] = '|' # make initial beam below source
    splits = 0
    for row in range(1, len(lines) - 1):
        for col in range(len(lines[row])):
            if lines[row][col] == "|":
                if lines[row + 1][col] == '^':
                    splits += 1
                    # These may overwrite each other, but this means we never count duplicates
                    lines[row + 1][col - 1] = '|'
                    lines[row + 1][col + 1] = '|'
                else:
                    lines[row + 1][col] = '|'
    print(splits)
