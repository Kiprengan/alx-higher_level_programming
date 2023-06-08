#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argnum = len(sys.argv)
    if argnum == 1:
        print("{} arguments.".format(argnum - 1))
    elif argnum == 2:
        print("{} argument:".format(argnum - 1))
    else:
        print("{} arguments:".format(argnum - 1))

    for m in range(1, argnum):
        print("{}: {}".format(m, sys.argv[m]))
