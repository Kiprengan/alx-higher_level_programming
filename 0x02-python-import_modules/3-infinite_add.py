#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    rslt = 0
    arglen = len(sys.argv)
    for m in range(1, arglen):
        rslt += int(arglen[m])
    print("{}".format(rslt))
