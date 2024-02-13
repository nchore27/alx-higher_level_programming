#!/usr/bin/python3
for i in range(97, 123):
    if i == 101:
        i + 1
    elif i == 113:
        i + 1
    else:
        print("{}".format(chr(i)), end="")
