#!/usr/bin/env python3
import argparse
import hashlib
import time

parser = argparse.ArgumentParser()
parser.add_argument(
    '-f', help='file of the hashes you want to crack', dest='file')
parser.add_argument('-w', help='wordlist file in .txt format', dest='words')
args = parser.parse_args()

start = time.time()
file = args.file
words = args.words
end = 0
years = list(range(1990, 2001))
specials = ["@", "_", "!", "#", "$", "%", "^", "&", "*",
            "(", ")", "<", ">", "?", "/", "|", "}", "{", "~", ":", "]"]
results = []

with open('./{}'.format(words)) as f:
    words = f.read().splitlines()

with open('./{}'.format(file)) as f:
    hashes = f.read().splitlines()


#go through concatenations of words 
def concatenated():
    print("Bruteforcing concatenated words:")
    for x in words:
        if x == "yellow":
            for y in words:
                if hashlib.sha1(x.encode('utf-8') + y.encode('utf-8')).hexdigest() in hashes:
                    end = time.time()
                    print("Password found: {} it took {}".format(
                        x+y, end-start))
                    results.append(x+y)
#go through single word passwords 
def singleWord():
    print("Bruteforcing single words:")
    for x in words:
        if hashlib.sha1(x.encode('utf-8')).hexdigest() in hashes:
            end = time.time()
            print("Password found: {} it took {}".format(x, end-start))
            results.append(x)
            break

#append birthdate to a single word
def appendBirthdate():
    print("Bruteforcing appended birthdates:")
    for x in words:
        for year in years:
            if hashlib.sha1(x.encode('utf-8') + str(year).encode('utf-8')).hexdigest() in hashes:
                end = time.time()
                password = x + str(year)
                results.append(password)
                print("Password found: {} it took {}".format(password, end-start))
            if hashlib.sha1(x.encode('utf-8').capitalize() + str(year).encode('utf-8')).hexdigest() in hashes:
                    end = time.time()
                    password = x.capitalize() + str(year)
                    print("Password found: {} it took {}".format(password, end-start))
                    results.append(password)
                    break     

#append birthdate and special to single word
def appendBirthdateAndSpecial():
    print("Bruteforcing appended birthdate + special:")
    for x in words:
        for year in years:
            for special in specials:
                if hashlib.sha1(x.encode('utf-8') + str(year).encode('utf-8') + special.encode('utf-8')).hexdigest() in hashes:
                    end = time.time()
                    password = x + str(year)
                    print("Password found: {} it took {}".format(password, end-start))
                    results.append(password)
                if hashlib.sha1(x.encode('utf-8').capitalize() + str(year).encode('utf-8') + special.encode('utf-8')).hexdigest() in hashes:
                        end = time.time()
                        password = x.capitalize() + str(year)
                        print("Password found: {} it took {}".format(password, end-start))
                        results.append(password)
                        break     

#append special character to single word
def specialCharAppended():
    print("Bruteforcing appended special charactes:")
    for x in words:
        for special in specials:
            if hashlib.sha1(x.encode('utf-8') + special.encode('utf-8')).hexdigest() in hashes:
                end = time.time()
                print("Password found: {} it took {}".format(x + special, end-start))
                results.append(x + special)
                break

#special character in front of a word
def specialCharInFront():
    print("Bruteforcing special before word:")
    for x in words:
        for special in specials:
            if hashlib.sha1(special.encode('utf-8') + x.encode('utf-8')).hexdigest() in hashes:
                end = time.time()
                print("Password found: {} it took {}".format(special + x, end-start))
                results.append(special + x)
                break

#special char in fornt and after the word
def specialCharInFrontAndAppend():
    print("Bruteforcing special before and after:")
    for x in words:
        for s in specials:
            for s2 in specials:
                if hashlib.sha1(s.encode('utf-8') + x.encode('utf-8') + s2.encode('utf-8')).hexdigest() in hashes:
                    end = time.time()
                    print("Password found: {} it took {}".format(s + x + s2, end-start))
                    results.append(s+x+s2)
                if hashlib.sha1(s.encode('utf-8') + x.encode('utf-8').capitalize() + s2.encode('utf-8')).hexdigest() in hashes:
                    end = time.time()
                    print("Password found: {} it took {}".format(s + x.capitalize() + s2, end-start))
                    results.append(s + x.capitalize() + s2)
                    break

#you can try this if you want, will probably run years
def allCombinations():
    print("Trying out all the hints")
    for x in words:
        for y in words:
            for s in specials:
                for year in years:
                    print(x.capitalize() + y.capitalize() + str(year) + s)
                    if hashlib.sha1(x.capitalize().encode('utf-8') + y.capitalize().encode('utf-8') + str(year).encode('utf-8') + s.encode('utf-8')).hexdigest() in hashes:
                        end = time.time()
                        print("Password found: {} it took {}".format(x.capitalize() + y.capitalize + str(year) + s, end-start))

if __name__ == "__main__":
    concatenated()
    singleWord()
    appendBirthdate()
    specialCharInFront()
    specialCharInFrontAndAppend()
    appendBirthdateAndSpecial()
    #allCombinations()
    print("Bruteforcing stopped")
    overallTime = time.time()
    print("Overall this took: {}".format(overallTime-start))
    with open('passwords.txt', 'w') as filehandle:
        for x in results:
            filehandle.write('%s\n' % x)