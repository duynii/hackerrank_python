import numpy

n, m = map(int, input().split())

mat = []
for _ in range(n):
    mat.append( list(map(int, input().split())) )
    
print( numpy.mean(mat, axis = 1) )
print( numpy.var(mat, axis=0) )
print( numpy.std(mat) )
