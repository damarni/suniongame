#!/usr/bin/env python
from os import chdir
from subprocess import call, check_output
from sys import argv

LEVELS = 512

def decompress(fin):
    output = str(check_output(['file', fin])).lower()
    if 'rar' in output:
        call(['rar', 'x', fin])
        call(['rm', fin])
    elif 'xz' in output:
        call(['tar', 'xvJf', fin])
        call(['rm', fin])
    elif 'tar' in output:
        call(['tar', 'xvf', fin])
        call(['rm', fin])
    elif 'gzip' in output:
        call(['tar', 'zxvf', fin])
        call(['rm', fin])
    elif 'zip' in output:
        call(['unzip', fin])
        call(['rm', fin])
    else:
        print("Finished!")


# Starting with file 512.*, extracts everything.
if __name__ == '__main__':
    chdir('files/')
    for i in reversed(range(0, LEVELS+1)):
        decompress(str(i))
