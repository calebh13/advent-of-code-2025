# the only difference here is we don't even have to search the intervals, just count the number of IDs in each range through a simple subtraction
# this is much easier since we merged the intervals :)

# INPUT_FILE = r"day 5/test.txt"
INPUT_FILE = r"day 5/input.txt"

from typing import List

def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged = []
    for interval in intervals:
        if merged and merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged

def searchIntervals(intervals: List[List[int]], id: int) -> int:
    left, right = 0, len(intervals) - 1
    while left <= right:
        mid = (left + right) // 2
        if intervals[mid][0] <= id <= intervals[mid][1]:
            return mid
        elif intervals[mid][1] < id:
            # Go right
            left = mid + 1
        else:
            # Go left (intervals[mid][0] > id)
            right = mid - 1
    return -1

if __name__ == "__main__":
    intervals = []
    ids = []
    with open(INPUT_FILE) as file:
        for line in file:
            if line == "\n":
                break
            intervals.append([int(num) for num in line.split("-")])
        for line in file: # iterator is partially consumed, so this starts right where we left off
            ids.append(int(line))
    
    intervals = mergeIntervals(intervals)

    freshCount = 0
    for interval in intervals:
        freshCount += (interval[1] - interval[0] + 1)
        print(f"IDs {interval[0]} through {interval[1]} are fresh")
    
    print(freshCount)
