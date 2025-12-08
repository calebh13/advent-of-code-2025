# INPUT_FILE = r"day 6/test.txt"
INPUT_FILE = r"day 6/input.txt"

if __name__ == "__main__":
    lines = []
    with open(INPUT_FILE, "r") as file:
        for line in file: 
            lines.append([int(num) if num.isdigit() else num for num in line.split()])
    
    grandTotal = 0
    for col, op in enumerate(lines[-1]):
        match(op):
            case '*':
                prod = 1
                for i in range(len(lines) - 1):
                    prod *= lines[i][col]
                grandTotal += prod
            case '+':
                s = 0
                for i in range(len(lines) - 1):
                    s += lines[i][col]
                grandTotal += s
            case _:
                raise ValueError
              
    print(grandTotal)
