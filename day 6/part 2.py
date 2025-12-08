# INPUT_FILE = r"day 6/test.txt"
INPUT_FILE = r"day 6/input.txt"

if __name__ == "__main__":
    lines = []
    with open(INPUT_FILE, "r") as file:
        for line in file: 
            lines.append(line[:-1] + " " + line[-1:])
    
    grandTotal = 0
    for col, char in enumerate(lines[-1]):
        if char.isspace():
            continue
        # For something like
        # 123
        #  45
        #   6
        # *
        # we'll build the numbers by traversing each column
        # do this for each column, and add/multiply (in this case multiply) the results
        # once we get to a column that's all whitespace (i.e. the number we built is 0), we can stop.
        problemAnswer = 0 if char == '+' else 1
        while True:
            num, powTen = 0, 0
            for row in range(len(lines) - 2, -1, -1): # go UP the list since most significant digit is at the top
                if lines[row][col] != ' ':
                    num += int(lines[row][col]) * pow(10, powTen)
                    powTen += 1
            if num == 0:
                break # we've reached the last column
            problemAnswer = problemAnswer + num if char == '+' else problemAnswer * num
            col += 1
        grandTotal += problemAnswer
        
            
    print(grandTotal)
