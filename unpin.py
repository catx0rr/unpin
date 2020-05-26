#!/usr/bin/env python

'''
    unpin.py -- Simple 4-digit passwordlist generator

    Note:
        Modify the script for bruteforcing can be used as password list for 4-digit pins
'''

from itertools import product


filename = 'pin.txt'

def generate_pin():

    with open(filename, 'w') as pinfile:

        for i in product(range(10), repeat=4):
            pinfile.write('%s\n' % ''.join(map(str, i)))

        pinfile.close()


if __name__ == '__main__':
    generate_pin()
