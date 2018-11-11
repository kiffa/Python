def fib_x(n):
    a,b=(0,1)
    count=1
    while count<n:
        a,b=b,a+b
        count=count+1
a = fib_x(3)
print(a)
