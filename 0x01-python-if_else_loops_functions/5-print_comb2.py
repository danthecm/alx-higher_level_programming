#!/usr/bin/python3
for i in range(0, 100):
    print(
            "{}".format(i if i > 9 else f"0{i}"),
            end="{}".format(", " if i < 99 else "\n")
        )
