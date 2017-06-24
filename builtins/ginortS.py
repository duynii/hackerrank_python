s  = input()

def sorta(c):
    if c.isdigit():
        if (int(c) % 2) > 0:
            return ord(c) + 1000
        else:
            return ord(c) + 2000
    elif c.isupper():
        return ord(c) + 200
    else:
        return ord(c)

print( *sorted(s, key=sorta), sep=''  )
