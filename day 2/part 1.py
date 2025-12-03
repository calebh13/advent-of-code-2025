# to determine an invalid ID:

# 1. calculate n = number of digits. if it's odd, it cannot be invalid!
# 2. cut it in half. upper part = id // (10**(n/2)), lower part = id % (10**(n/2))
# 3. if upper part == lower part, we're done. 

# but iterating through each possible number and checking them all individually would be very slow.
# instead, we'll generate them.

# consider a range like [17330, 35281]. since they both have n=5 (odd), we can't generate any.

# or a range like [880610, 895941]. what we'll do is:
# start at x = 880610 (the lower bound).
# if the lower part of x is greater than the higher part, (e.g. if x was 100610), we'd
# do x += 10**(n/2) - since otherwise 100100 wouldn't be in the interval. in this case, we're fine.
# also, subtract lower part for convenience, so now x = 880000.

# then construct the first invalid ID by taking x + upper part. add it to the sum.
# next we need to do x += (10**(n/2)), so x = 881000 to continue constructing ids.
# then construct the ID by doing the same as before: x + upper part // (10**(n/2)), so id=881881.
# at each point, check that we're less than the upper bound; if not, quit, and move on to the next interval. 

# consider a range like [942, 1415]. if we ever get to a point where we have odd digits (n % 2 == 1),
# then set x = 10**(num_digits(x)+1), and continue on, making sure to do bounds checks.

# i would do leetcode #56 (merge intervals) on this input to save time, but it looks like none of them are overlapping.

def numDigits(x: int) -> int:
    digits = 0
    while x > 0:
        digits += 1
        x //= 10

    return digits

# Assumes x has even number of digits; returns (upper, lower) parts of x
def splitNum(x: int) -> tuple[int, int]:
    n = numDigits(x)
    return (x // pow(10, n // 2), x % pow(10, n // 2))

#INPUT_FILE = r"day 2/test.txt"
INPUT_FILE = r"day 2/input.txt"

if __name__ == "__main__":
    idSum = 0
    with open(INPUT_FILE, "r") as file:
        line = file.readline()
        intervals = [[int(num) for num in interval.split("-")] for interval in line.split(",")]
        for interval in intervals:
            id = interval[0]

            upper, lower = splitNum(id)
            id -= lower # for convenience, so we don't have to subtract lower each time
            if lower > upper: # 100610 case, where 100100 wouldn't be in the range
                id += pow(10, numDigits(id) // 2)

            while True:
                if (numDigits(id) % 2 == 1):
                    id = pow(10, numDigits(id)) # e.g. 942 -> 1000 since odd digits are useless
                upper, lower = splitNum(id)
                invalidId = id + upper
                if invalidId <= interval[1]: # make sure we're still in the interval before adding
                    idSum += invalidId
                    id += pow(10, numDigits(id) // 2) # increment id by 1 in the lowest digit of upper half
                else:
                    break
                
            
    print(idSum)
