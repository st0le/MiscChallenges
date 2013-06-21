# You can code in Python

import sys


def number2words(n):
    words = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
             10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
             18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',
             90:'ninety'}
    parts = {100:'hundred',1000:'thousand',1000000:'million'}
    def recurse(x):
        if x in words:
            return words[x]
        if x < 100:
            return "%s-%s" % (words[x-x%10],words[x%10])
        for part in reversed(sorted(parts)):
            if x >= part:
                return "%s-%s" %(recurse(x/part),parts[part]) + ("-" + recurse(x%part) if x % part > 0 else "")
    return recurse(n)

print '\n'.join(map(number2words,map(int,sys.stdin.readlines())))