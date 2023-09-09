#
# Calculates the Linn number of an integer.
#
# The Linn number is defined by the number of tries it takes to return to the original number
# given the pattern:
#   - Descend by triangular numbers until reaching 0 or would go below 0.
#   - Ascend by 2x triangular numbers until reaching our number or would go above.
#
# If we get stuck in an infinite loop, the linn number is 0.
# For the purposes of this script if we try more than MAX_TRIES then we return -1.
#
# Usage:
#    python3 linn_number.py <test num>
#    python3 linn_number.py <lowest test num> <highest test num>
# i.e:
#    # Tests the number 100
#    python3 linn_number.py 100
#    # Tests all numbers between 1 and 100 (inclusive)
#    python3 linn_number.py 1 100
#
import sys

MAX_TRIES = 100

def doCalc(num, verbose=False):
    nextAdd = 1
    current = num
    descending = True
    tries = 1
    turnArounds = {}

    if verbose:
        print("Beginning descent at", current)

    while tries < MAX_TRIES:

        # Descending
        if descending:
            if current - nextAdd < 0:
                if verbose:
                    print("Beginning ascent at", current)
                nextAdd = 2
                descending = False

            else:
                current -= nextAdd
                nextAdd += 1

        # Ascending
        else:
            if current + nextAdd == num:
                if verbose:
                    print("Reached", num, "again after", tries, "tries!")
                return tries

            # If we're going up and we will be too high, switch sides
            elif current + nextAdd > num:
                if verbose:
                    print("End try", tries, "beginning descent at", current)
                nextAdd = 1
                descending = True
                tries += 1
                if current in turnArounds:
                    if verbose:
                        print("Got back to", current, "which means we are in an infinite loop")
                    return 0
                turnArounds[current] = True

            else:
                current += nextAdd
                nextAdd += 2


    print("Reached max tries without getting back to  our number!")
    return -1

def doSingleCalc(num):
    tries = doCalc(num, verbose=True)
    print(num, "tries", tries)

def doCalcBetween(startNum, endNum):
    if startNum < 1:
        raise "Start num cannot be below 1"

    for i in range(startNum, endNum + 1):
        tries = doCalc(i)
        print(i, "tries", tries)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""
Bad Matt. Usage:
    python3 linn_number.py <test num>
    python3 linn_number.py <lowest test num> <highest test num>
i.e:
    python3 linn_number.py 100
    python3 linn_number.py 1 100
""")
        exit()

    low = int(sys.argv[1])

    high = 0
    if len(sys.argv) > 2:
        high = int(sys.argv[2])
        doCalcBetween(low, high)
    else:
        doSingleCalc(low)
