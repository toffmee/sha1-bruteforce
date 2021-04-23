#!/usr/bin/env python3

import argparse
import hashlib
import os
import re
import time
import sys 

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='file of the hashes you want to crack', dest='file')
parser.add_argument('-t', help='nr. of threads', dest='threads', type=int)
parser.add_argument('-w', help='wordlist file in .txt format', dest='words')
args = parser.parse_args()

start = time.time()
file = args.file
threads = args.threads or 4
words = args.words
attemptCount = 0
end = 0

with open('./{}'.format(words)) as f:
    words = f.read().splitlines()

with open('./{}'.format(file)) as f:
    hashes = f.read().splitlines()

if len(sys.argv) != 3:
    for x in words:
        if x == "yellow":
            for y in words:
                attemptCount += 1
                if hashlib.sha1(x.encode('utf-8') + y.encode('utf-8')).hexdigest() in hashes:
                    end = time.time()
                    print("Password found: {} it took {}".format(x+y, end-start))

    # for x in words:
    #     if hashlib.sha1(x.encode('utf-8')).hexdigest() in hashes:
    #         end = time.time()
    #         print("Password found: {} it took {}".format(x, end-start))
