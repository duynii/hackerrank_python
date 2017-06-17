n, x = map(int, input().split())

subjects = []
for _ in range(x):
    subjects.append( list(map(float, input().split())) )
    
for tup in zip(*subjects):
    print( sum(tup) / len(tup) )
