from timeit import timeit

def sum1(n):
    s = 0
    for i in range(n):
        s += i
    return s
    #print(s)

def sum2(n):
    s = sum(range(n))
    return s

# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('sum1(10000000)', 'from __main__ import sum1', number=1)
print(t)
t = timeit('sum2(10000000)', 'from __main__ import sum2', number=1)
print(t)
