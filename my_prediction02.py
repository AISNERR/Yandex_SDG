from mpmath import findroot, atanh

def f(y,t):
    return  t * 32 == y + 23

t = 1
print(fsolve(f, 100, args=(t)))