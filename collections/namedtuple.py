#!/usr/bin/python3
from collections import namedtuple
n = int(input())
cols = list(input().split())

Student = namedtuple('Student', ' '.join(cols))

total = 0.0
for i in range(n):
    line = input().split()
    s = Student(*line)
    total += float(s.MARKS) 
    
print( "{:0.2f}".format(total / n) )
