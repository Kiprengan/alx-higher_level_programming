#!/usr/bin/python3
for p in range(97, 123):
    if (p == 101) or (p == 113):
        continue
    print("{}".format(chr(p)), end="")
