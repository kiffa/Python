#验证哥德巴赫猜想之一：
#2000以内的正偶数（大于等于4）都能够分解为两个质数之和。
#每个偶数表达成形如：4=2+2的形式，输出时每行显示6个式子。
#首先需要一个函数用来判断分解出的数字是否是质数。

from math import sqrt
import time
start = time.time()
def is_prime(n):
    if n == 1:
        return False
    if n>10:
        if n %3 == 0:
            return False
        elif n % 5 == 0:
            return False
        elif n %7 == 0 : 
            return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

m=4
count=0
while m<2000:
    i =2
    while i<m:
        if is_prime(i) and is_prime(m-i):
            count +=1
            if count %6 != 0:
                print("{}={}+{}".format(m,i,m-i),end=' ')
            else:
                #print("{}={}+{}".format(m,i,m-i))
                print('\n')
            m += 2
            break
        else:
            i +=1
print('\n')
end = time.time()           #结束时间                   
print(end - start)          #输出运行时间
