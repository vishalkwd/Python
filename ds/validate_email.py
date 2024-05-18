import re

def fun(s):
    if re.match(r'^[A-Za-z0-9_-]+\@{1}([A-Za-z0-9])+\.{1}([A-Za-z]){1,3}$', s):
        return True
    else:
        return False

l = ["lara@hackerrank.com","brian-23@hackerrank.com","britts_54@hackerrank.com","itsme@gmail","@something","@something.com","@something.co1","sone.com","its@gmail.com1","mike13445@yahoomail9.server","rase23@ha_ch.com","daniyal@gmail.coma","thatisit@thatisit"]

for i in l:
    print(f"{i}:     {fun(i)}")