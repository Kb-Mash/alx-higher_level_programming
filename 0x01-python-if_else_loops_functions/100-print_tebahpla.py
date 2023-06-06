#!/usr/bin/python3
for alph in range(ord('z'), ord('a') - 1, -1):
    if alph % 2 == 0:
        i = 0
    else:
        i = 32
    print('{}'.format(chr(alph - i)), end='')
