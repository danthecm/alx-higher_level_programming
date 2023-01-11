#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j:
            continue
        if int(f"{i}{j}") > 9:
            if i > j:
                continue
        if f"{i}{j}" != "89":
            print("{}{}".format(i, j), end=", ")
        else:
            print("{}{}".format(i, j), end="\n")
