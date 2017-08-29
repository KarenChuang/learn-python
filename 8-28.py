def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2,0))

def fun(a, b = 1, c = 2):
    print(a)
    print(b)
    print(c)

fun(1,33)
