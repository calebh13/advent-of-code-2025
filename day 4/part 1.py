INPUT_FILE = r"day 4/input.txt"
# INPUT_FILE = r"day 4/test.txt"

NEIGHBORS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

if __name__ == "__main__":
    idSum = 0
    grid = []
    def adjacentRolls(row: int, col: int) -> int:
        count = 0
        for dX, dY in NEIGHBORS:
            nRow = row + dY
            if 0 <= nRow < len(grid):
                nCol = col + dX
                if 0 <= nCol < len(grid[nRow]) and grid[nRow][nCol] == '@':
                    count += 1
        return count

    with open(INPUT_FILE, "r") as file:
        for line in file:
            grid.append(line)
    
    accessibleRolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@' and adjacentRolls(row, col) < 4:
                accessibleRolls += 1
    
    print(accessibleRolls)
