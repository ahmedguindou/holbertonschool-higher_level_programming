#!/usr/bin/python3
def uppercase(str):
    num = 0
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            num = 32
        else:
            num = 0
        print('{:c}'.format(ord(c) - num), end="")
    print()
