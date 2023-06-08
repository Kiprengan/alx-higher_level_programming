#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    totalResult = 0
    for m in range(len(sys.argv) - 1):
        totalResult += int(sys.argv[m + 1])
    print("{}".format(totalResult))
