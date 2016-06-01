#!/usr/bin/env python
from itertools import product
from string import ascii_lowercase
from subprocess import call

MAX_LENGTH = 6

if __name__ == '__main__':
    with open('/dev/null', 'w') as devnull:
        for l in range(1, MAX_LENGTH):
            print('Trying words with length {0}...'.format(l))
            for perm in product(ascii_lowercase, repeat=l):
                pswd = ''.join(list(perm))
                if call(['unzip', '-t', '-P', pswd, '-qq', '-o', 'input'], 
                        stderr=devnull, stdout=devnull) == 0:
                    call(['unzip', '-o', '-P', pswd, 'input'])
                    print('Extracted Zip with password: {0}'.format(pswd))
                    exit()
        print('No password found up to length {0} to extract zip'.format(MAX_LENGTH))
