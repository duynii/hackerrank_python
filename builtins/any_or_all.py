n = map(int, input().split())
data = list(map(int, input().split()))

# n=aabbcc
# n[::-1] reverses the string, hence compare with n to check for palindromic string
print( all([x>0 for x in data]) and any( str(x) == str(x)[::-1] for x in data ) )
