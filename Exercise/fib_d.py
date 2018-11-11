def fib_d(n):
    if n==0 or n==1:
        return n
    else:
        return fib_d(n-1) + fib_d(n-2)
a = fib_d(3)
print(a)
