# as preprocessing i'll do leetcode #56 merge intervals to speed up searching
# this also lets us do a binary search on the intervals

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
    for id in ids:
        if searchIntervals(intervals, id) != -1:
            freshCount += 1
            print(f"ID {id} is fresh")
    
    print(freshCount)
