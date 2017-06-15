import numpy
n, m = map(int, input().split())

mat = []
for _ in range(n):
    mat.append( list(map(int, input().split())) )
    
print( numpy.prod( numpy.sum( mat, axis = 0 ) ) )
