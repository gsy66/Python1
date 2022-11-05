def fbnq(n):
    n1 = 1
    n2 = 1
    n3 = 1
    a = 3

    if n < 1:
        print('输入错误')
        return -1
    if n ==1 or n == 2:
        return 1
    while a <= n:
        n3 = n1 +n2
        n1 = n2
        n2 = n3
        a = a+1
    return n3

a = int(input('输入所求的项数：'))

result = fbnq(a)
print('数列的第%d项是: %d ' % (a,result))
