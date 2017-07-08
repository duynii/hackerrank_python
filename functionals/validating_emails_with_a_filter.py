import re
def fun(s):
    # return True if s is a valid email, else return False
    return bool( re.match( r'^[a-zA-z-_0-9]+@[a-zA-Z0-9]+\.[a-z]{1,3}$', s) )
