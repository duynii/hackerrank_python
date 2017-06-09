#!/usr/bin/python3
from itertools import groupby

s = input()

# groups = []
# for key, g in groupby(s):
#     groups.append( ( len(list(g)), int(key) ) )
# print( *groups )

groups = [( len(list(g)), int(key) ) for key, g in groupby(s) ]
print( *groups ) # '*' change it to tuple 
