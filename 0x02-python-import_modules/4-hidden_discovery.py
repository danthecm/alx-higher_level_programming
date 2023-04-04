#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    module_names = dir(hidden_4)
    module_names = [name for name in module_names if name[0: 2] != "__"]
    for name in module_names:
        print(name)
