#!/usr/bin/python3
for dec in range(0, 100):
    if dec == 99:
        print('{:d}'.format(dec))
    else:
        print('{:02}'.format(dec), end=', ')
