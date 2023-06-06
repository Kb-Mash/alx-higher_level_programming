#!/usr/bin/python3
for dec in range(0, 100):
    if dec == 99:
        print(f'{dec:d}')
    else:
        print(f'{dec:02}', end=', ')
