#!/usr/bin/python3
for p in range(0, 10):
    for m in range(p + 1, 10):
        if p == 8 and m == 9:
            print("{}{}".format(p, m))
        else:
            print("{}{}".format(p, m), end=", ")
